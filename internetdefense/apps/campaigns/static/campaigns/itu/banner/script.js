(function($){

    $.fn.disableButton = function(options){
        var settings = $.extend( {
            'text': 'Working...',
            'class': 'disabled'
        }, options);
        return this.each(function(){
            var $button = $(this);
            $button.attr('disabled', 'disabled');
            $button.addClass(settings['class']);
            $button.data({
                '_oldtext': $button.text(),
                '_settings': settings
            });
            $button.text(settings['text']);
        });
    };

    $.fn.enableButton = function(options){
        return this.each(function(){
            var $button = $(this),
                settings = $button.data('_settings');
            $button.removeAttr('disabled');
            $button.removeClass(settings['class']);
            $button.text($button.data('_oldtext'));
        });
    };

    $(function(){

        Placeholders.init();

        $(document).delegate('#action', 'submit', function(evt){
            evt.preventDefault();
        });

        $(document).delegate('#button_email', 'click', function(evt){
            evt.preventDefault();
            var $button = $(this),
                $email = $('[name="Email"]'),
                $phone = $('[name="Phone"]'),
                $country = $('[name="Country"]'),
                hasError = false;

            if($button.is(':disabled')){
                return;
            }

            $button.disableButton();

            // Require email address
            if(!$email.val()){
                $email.addClass('error');
                hasError = true;
            }else{
                $email.removeClass('error');
            }

            if(!hasError){
                $button.text('Thanks!').attr('id', 'button_thanks');
                if($country.val() !== ''){
                    var responder = responderMap.hasOwnProperty($country.val()) ? parseInt(responderMap[$country.val()], 10) : 209;
                    $.get('https://nt.salsalabs.com/save', {
                        'object': $('[name="object"]').val(),
                        'tag': $('[name="tag"]').val(),
                        'ip': $('[name="ip"]').val(),
                        'user_agent': $('[user_agent="object"]').val(),
                        'email_trigger_KEYS': responder,
                        'organization_KEY': $('[name="organization_KEY"]').val(),
                        'redirect': $('[name="redirect"]').val(),
                        'Email': $('[name="Email"]').val(),
                        'Phone': $('[name="Phone"]').val(),
                        'Country': $('[name="Country"]').val(),
                        'organizer': $('[name="organizer"]').val()
                    });
                    window.open('http://www.internetcoup.org/?email_action', 'itu_email');
                }else{
                    window.open('http://www.internetcoup.org/?no_country&Phone=' + encodeURIComponent($phone.val()) + '&Email=' + encodeURIComponent($email.val()), 'itu_call');
                }

            }else{
                $button.enableButton();
            }



        });

        $('#button_call').show();
        $(document).delegate('#button_call', 'click', function(evt){
            evt.preventDefault();
            var $button = $(this),
                $email = $('[name="Email"]'),
                $phone = $('[name="Phone"]'),
                $country = $('[name="Country"]'),
                hasError = false;

            if($button.is(':disabled')){
                return;
            }

            $button.disableButton();

            // Require phone number
            if(!$phone.val()){
                $phone.addClass('error');
                hasError = true;
            }else{
                $phone.removeClass('error');
            }

            if(!hasError){
                $button.text('Thanks!').attr('id', 'button_thanks');
                if($country.val() !== ''){
                    $.post('http://www.internetcoup.org/en/calltool/', {
                        'number': $('[name="Phone"]').val(),
                        'country': $('[name="Country"]').val()
                    });
                    window.open('http://www.internetcoup.org/?call_action', 'itu_call');
                }else{
                    window.open('http://www.internetcoup.org/?no_country&Phone=' + encodeURIComponent($phone.val()) + '&Email=' + encodeURIComponent($email.val()), 'itu_call');
                }
            }else{
                $button.enableButton();
            }
        });

    });

})(jQuery);

(function($){

    window.IDL = {

        'CustomIncludeCode': function(){
            var output = $('[name="output"]'),
                variants = $('[name="variant"]'),
                campaignChoose = $('[name="campaign"]'),
                allCampaigns = $('#all'),
                singleCampaign = $('#single'),
                campaignChoice = $('[name="campaign_choice"]'),
                configString = function(name, value){
                    if(value){
                        return '\n    _idl.' + name + ' = "' + value + '";';
                    }else{
                        return '';
                    }
                };

            output.data('template', output.val());
            this.update = function(){
                var new_code = output.data('template');
                new_code = new_code.replace('{variant}', configString('variant', $('[name="variant"]:checked').val()));
                new_code = new_code.replace('{campaign}', configString('campaign', $('[name="campaign"]:checked').val()));
                output.val('<script type="text/javascript">\n' + new_code + '\n</script>');
            };
            this.update();

            var self = this;

            $(window).bind('unload', function(evt){
                output.val(output.data('template'));
            });

            variants.bind('change', function(evt){
                var target = $(evt.target),
                    allVariants = variants.closest('div');
                allVariants.removeClass('indented').removeClass('light');
                target.closest('div').addClass('indented').addClass('light');
                self.update();
            });

            campaignChoice.bind('change', function(evt){
                singleCampaign.attr('value', campaignChoice.val());
                self.update();
            });

            allCampaigns.bind('change', function(evt){
                singleCampaign.attr('value', '');
                self.update();
            });

            singleCampaign.bind('change', function(evt){
                // singleCampaign.attr('value', campaignChoice.val());
                   singleCampaign.attr('value', 'cispa')
                self.update();
            });

            campaignChoose.bind('change', function(evt){
                var target = $(evt.target),
                    allVariants = campaignChoose.closest('div');
                allVariants.removeClass('indented').removeClass('light');
                target.closest('div').addClass('indented').addClass('light');
            });

        }

    };
    
    $(function() {

        var include = new IDL.CustomIncludeCode();

    });
    

	$(".large textarea").focus(function() {
	    var $this = $(this);
	    $this.select();

	    // Work around Chrome's little problem
	    $this.mouseup(function() {
	        // Prevent further mouseup intervention
	        $this.unbind("mouseup");
	        return false;
	    });
	});


})(jQuery);

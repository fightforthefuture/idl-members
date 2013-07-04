{% load minify %}


    {% include 'include/js/lib/closure_start.js' %}
    {% include 'include/js/lib/cookies.js' %}
    {% include 'include/js/lib/querystring.js' %}
    {% include 'include/js/lib/addevent.js' %}
    {% include 'include/js/lib/classname.js' %}

    // Default settings
    var qs = querystring.decode(),
        canPostMessage = !!window.postMessage,
        defaults = {
            'variant': 'banner',
            'campaign': null,
            'url': null,
            'cookieLength': 24 * 60 * 60 * 1000,
            'test': Boolean(parseInt(qs._idl_test, 2))
        },
        ieQuirks = (document.compatMode != 'CSS1Compat') && (navigator.appVersion.indexOf("MSIE") != -1);

    // Overrides defaults with settings in window._idl
    for(var key in _idl){
        if(_idl.hasOwnProperty(key)){
            defaults[key] = _idl[key];
        }
    }

    // Ensure that user hasn't opted out
    var cookieName = '_idl_opt_out_' + '{{ campaign.slug }}',
        opted_out = cookie.read(cookieName) == 'true';

    // disable mobile and small screens
    if(!(window.innerWidth <= 800 && window.innerHeight <= 800)){

     if(!opted_out || defaults.test){

        // Caches settings serialization and fetch of body element
        var settings = querystring.encode(defaults),
            head = document.getElementsByTagName('head')[0],
            body = document.getElementsByTagName('body')[0],
            html = document.getElementsByTagName('html')[0],
            ifr, ifr_src;

        if(ieQuirks){
            className.add(html, 'idl_ie_quirks');
        }

        // Sets frame URL
        if(defaults.test){
            ifr_src = '{{ SECURE_STATIC_URL }}campaigns/test/' + defaults.variant + '.html?' + settings;
        }else if(defaults.url){
            ifr_src = defaults.url;
        }else{
            ifr_src = '//{{ INCLUDE_DOMAIN }}{{ url }}';
        }


        // Creates and appends iframe element containing content
        ifr = document.createElement('iframe');
        ifr.type = 'text/javascript';
        ifr.async = true;
        ifr.scrolling = 'no';
        ifr.frameBorder = 0;
        ifr.id = 'idl_alert';
        ifr.src = ifr_src;
        className.add(html, 'idl_' + defaults.variant);
        body.appendChild(ifr);

        {% if variant == 'modal' %}

            var metatags = document.getElementsByTagName('meta'),
                oldViewport = null,
                newViewport;

            // Creates and appends iframe element containing content
            var backdrop = document.createElement('div');
            backdrop.id = 'idl_backdrop';
            body.appendChild(backdrop);

            // Creates and appends close bytton
            var closeBtn = document.createElement('a');
            closeBtn.id = 'idl_close';
            closeBtn.href = '#';
            closeBtn.innerHTML = 'x'
            body.appendChild(closeBtn);

            // Close modal and set opt-out cookie on click of close button,
            // backdrop, or <esc> press.
            var closeModal = function(evt){
                className.remove(html, 'idl_' + defaults.variant);
                if(!defaults.test){
                    cookie.write(cookieName, 'true', defaults.cookieLength);
                }
                ifr.parentNode.removeChild(ifr);
                backdrop.parentNode.removeChild(backdrop);
                closeBtn.parentNode.removeChild(closeBtn);
                if(oldViewport){
                    head.appendChild(oldViewport);
                }
                if(newViewport){
                    newViewport.parentNode.removeChild(newViewport);
                }
            };
            addEvent(closeBtn, 'click', closeModal);
            addEvent(backdrop, 'click', closeModal);
            addEvent(document, 'keyup', function(evt){
                if(evt.keyCode == 27){
                    closeModal(evt);
                }
            });

            // Send messages to set a class on the <html> tag of the included page
            if(canPostMessage){
                try{
                    var checkMobile = function(){
                        var message = '';
                        if(window.innerWidth <= 800 && window.innerHeight <= 800){
                            message = 'idl_mobile';
                            if(window.innerWidth > window.innerHeight){
                                message = message + ':idl_landscape';
                            }
                        }
                        ifr.contentWindow.postMessage(message, '*');
                    }
                    addEvent(window, 'resize', checkMobile);
                    addEvent(window, 'load', function(){
                        checkMobile();
                    });
                    checkMobile();
                }catch(err){}
            }

            // Find and store old viewport. If there is no old viewport, let's
            // create one with defaults to force iOS to redraw appropriately.
            // We'll update with our own, but restore the old one on close.
            try{
                for(var i in metatags){
                    var tag = metatags[i];
                    if(metatags.hasOwnProperty(i) && !!tag.nodeName && tag.name == 'viewport'){
                        oldViewport = tag;
                        oldViewport.parentNode.removeChild(oldViewport);
                        break;
                    }
                }
                if(!oldViewport){
                    oldViewport = document.createElement('meta');
                    oldViewport.name = 'viewport';
                    oldViewport.content = 'width=980, user-scalable=1';
                }
                newViewport = document.createElement('meta');
                newViewport.name = 'viewport';
                newViewport.content = 'width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0';
                head.appendChild(newViewport);
            }catch(err){}

        {% endif %}

        // Add CSS string
        var style = document.createElement('style'),
            rules = "{% include 'include/css/include.css' %}";
        style.type = 'text/css';
        head.appendChild(style);
        if(style.styleSheet){
            style.styleSheet.cssText = rules;
        }else{
            style.innerHTML = rules;
        }

    }

      } /* if tinyscreen() */

    {% include 'include/js/lib/closure_finish.js' %}

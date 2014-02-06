{% load minify %}


    {% include 'include/js/lib/closure_start.js' %}
    {% include 'include/js/lib/cookies.js' %}
    {% include 'include/js/lib/querystring.js' %}
    {% include 'include/js/lib/addevent.js' %}
    {% include 'include/js/lib/classname.js' %}

    /* Default settings */
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

    /* Overrides defaults with settings in window._idl */
    for(var key in _idl){
        if(_idl.hasOwnProperty(key)){
            defaults[key] = _idl[key];
        }
    }

    /* Ensure that user hasn't opted out */
    var cookieName = '_idl_opt_out_' + '{{ campaign.slug }}',
        opted_out = cookie.read(cookieName) == 'true';
    if (opted_out) {
        return;
    }

    /* Require modern browsers. */
    if (!document.addEventListener) {
        return;
    }

    /* Require all campaigns to be enabled. */
    if (_idl.variant !== 'banner' || _idl.campaign) {
        return;
    }

    /* The Day We Fight Back :: JavaScript */
    /* @license magnet:?xt=urn:btih:0b31508aeb0634b347b8270c7bee4d411b5d4109&dn=agpl-3.0.txt GPL-v3-or-Later */
    (function(){
        var e = document.createElement('script'); e.type='text/javascript'; e.async = true;
        e.src = document.location.protocol + '//d1agz031tafz8n.cloudfront.net/thedaywefightback.js/widget.min.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(e, s);
    })();
    /* @license-end */

    {% include 'include/js/lib/closure_finish.js' %}

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
            'variant': 'modal',
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
    if (_idl.variant !== 'modal' || (_idl.campaign && _idl.campaign !== 'reset-the-net')) {
        return;
    }

    var e = document.createElement('script'); e.type='text/javascript'; e.async = true;
    e.src = '//fightforthefuture.github.io/reset-the-net-widget/widget/rtn.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(e, s);

    {% include 'include/js/lib/closure_finish.js' %}

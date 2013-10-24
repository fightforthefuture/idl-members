{% load minify %}

    {% include 'include/js/lib/closure_start.js' %}
    {% include 'include/js/lib/cookies.js' %}
    {% include 'include/js/lib/querystring.js' %}

    // Ensure that user hasn't opted out.
    var cookieName = '_idl_opt_out_' + '{{ campaign.slug }}',
        optedOut = cookie.read(cookieName) == 'true';

    if (optedOut) {
        return;
    }

    // Verify campaign.
    var qs = querystring.decode();
    if (_idl.campaign && _idl.campaign !== 'stopwatchingusrally') {
        return 'Bailing';
    }

    // Set variant.
    var variant = 'default';
    if (qs.variant === 'modal') {
        variant = 'modal';
    }

    window.tfrce_config = {
        show_style: variant
    };

    {% include 'include/js/lib/megaphone.js' %}

    {% include 'include/js/lib/closure_finish.js' %}

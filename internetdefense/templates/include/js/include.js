{% load minify %}

    {% include 'include/js/lib/closure_start.js' %}
    {% include 'include/js/lib/cookies.js' %}
    {% include 'include/js/lib/querystring.js' %}

    // Ensure that user hasn't opted out
    var cookieName = '_idl_opt_out_' + '{{ campaign.slug }}',
        optedOut = cookie.read(cookieName) == 'true';

    if (optedOut) {
        return;
    }

    {% include 'include/js/lib/megaphone.js' %}

    {% include 'include/js/lib/closure_finish.js' %}

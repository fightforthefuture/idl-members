(function(){
    function detectUnsupportedBrowser() {
        var unsupported = false;
        if (navigator.appName == 'Microsoft Internet Explorer') {
            var ua = navigator.userAgent;
            var re  = new RegExp("MSIE ([0-8]{1,}[\.0-8]{0,})");
            if (re.exec(ua) != null) {
                unsupported = true;
            }
        }
        return unsupported;
    }

    if (detectUnsupportedBrowser()) {
        return;
    }

    window.tfrce_config = {
        // debug: true,
        disableGeo: true // If true, will show to all visitors not just those around Washington DC
    };

    var e = document.createElement('script'); e.type='text/javascript'; e.async = true;
    e.src = document.location.protocol + '//d1ux67szpr7bp0.cloudfront.net/project-megaphone/widget.min.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(e, s);
})();

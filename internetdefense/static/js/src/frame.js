var qs = querystring.decode(),
    html = document.getElementsByTagName('html')[0],
    body = document.getElementsByTagName('body')[0],
    supportsTouch = !!('ontouchstart' in window),
    uaInput = document.getElementById('user_agent'),
    ipInput = document.getElementById('signup_ip'),
    ipScript = document.createElement('script'),
    ieQuirks = (document.compatMode != 'CSS1Compat') && (navigator.appVersion.indexOf("MSIE") != -1);

window.getip = function(json){
    ipInput.value = json.ip;
};

className.add(html, ' idl_' + qs.variant);

if(supportsTouch){
    className.add(html, 'idl_touch');
}

if(ieQuirks){
    className.add(html, 'idl_ie_quirks');
}

addEvent(window, 'message', function(evt){
    if(evt.data === ''){
        className.remove(html, 'idl_mobile');
        className.remove(html, 'idl_landscape');
    }else{
        var messages = evt.data.split(':'),
            isMobile = messages[0] == 'idl_mobile',
            isLandscape = messages[1] == 'idl_landscape';
        if(isMobile){
            className.add(html, 'idl_mobile');
        }else{
            className.remove(html, 'idl_mobile');
        }
        if(isLandscape){
            className.add(html, 'idl_landscape');
        }else{
            className.remove(html, 'idl_landscape');
        }
    }
});

addEvent(window, 'load', function(evt){
    uaInput.value = navigator.userAgent;
    ipScript.type = 'text/javascript';
    ipScript.src = '//fftf-ips.heroku.com/?callback=getip';
    body.appendChild(ipScript);
});

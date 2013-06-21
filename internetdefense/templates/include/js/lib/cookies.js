/*
 *  Simplified interface for working with cookies.
 *  Adapted from http://www.quirksmode.org/js/cookies.html
 *
 *  Functions:
 *    cookie.write - Writes cookie
 *    cookie.read - Returns value of cookie
 *    cookie.delete - Deletes cookie
 *
 *  Example:
 *    >>> cookie.read('foo');
 *    null
 *    >>> cookie.write('foo', 'bar');
 *    >>> cookie.read('foo');
 *    'bar'
 *    >>> cookie.delete('foo');
 *    >>> cookie.read('foo');
 *    null
 */

var cookie = {

    'write': function(name, value, length) {
        var date = new Date();
        date.setTime(date.getTime() + length);
        document.cookie = name + '=' + value + '; expires=' + date.toGMTString() + '; path=/';
    },

    'read': function(name) {
        var nameEq = name + '=';
        var ca = document.cookie.split(';');
        for(var i=0; i < ca.length; i++) {
            var c = ca[i];
            while(c.charAt(0) == ' '){
                c = c.substring(1, c.length);
            }
            if(c.indexOf(nameEq) === 0){
                return c.substring(nameEq.length, c.length);
            }
        }
        return null;
    },

    'delete': function(name){
        this.write(name, '', -1);
    }

};

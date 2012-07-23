/*
 *  Simplified interface for working with querystring parameters.
 *
 *  Functions:
 *    querystring.encode - creates serialized representation of an object,
 *      suitable for use in a querystring
 *    querystring.decode - deserializes querystring into object literal
 *
 *  Example on http://example.tld/?foo=bar&baz=qux
 *    >>> querystring.decode();
 *    {foo: 'bar', baz: 'qux'}
 *    >>> querystring.encode({foo: 'bar', baz: 'qux'})
 *    foo=bar&baz=qux
 */

var querystring = {

    encode: function(obj){
        var bits = [];
        for(var bit in obj) {
            if(obj.hasOwnProperty(bit)) {
                var key = encodeURIComponent(bit),
                    value = encodeURIComponent(obj[bit]);
                bits.push(key + '=' + value);
            }
        }
        return bits.join("&");
    },

    decode: function(){
        var urlParams = {},
            plusToSpace = /\+/g,
            search = /([^&=]+)=?([^&]*)/g,
            decode = function(s){
                return decodeURIComponent(s.replace(plusToSpace, ' '));
            },
            query  = window.location.search.substring(1);
        while(match = search.exec(query)){
            urlParams[decode(match[1])] = decode(match[2]);
        }
        return urlParams;
    }

};
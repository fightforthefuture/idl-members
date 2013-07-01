/*
 *  Simplified interface for adding/removing classes to DOM elements
 *
 *  Functions:
 *    className.add - adds a class
 *    className.remove - removes a class
 *
 *  Example:
 *    >>> body = document.getElementsByTagName('body')[0];
 *    >>> body.className
 *    ''
 *    >>> className.add(body, 'foo');
 *    >>> body.className
 *    'foo'
 *    >>> className.remove('foo');
 *    >>> body.className
 *    ''
 */

var className = {

    'regex': function(className){
        return new RegExp('(\\s|^)' + className + '(\\s|$)', 'gi');
    },

    'add': function(elem, className){
        if(!elem.className.match(this.regex(className))){
            elem.className = elem.className + ' ' + className;
        }
    },

    'remove': function(elem, className){
        elem.className = elem.className.replace(this.regex(className), ' ');
    }

};

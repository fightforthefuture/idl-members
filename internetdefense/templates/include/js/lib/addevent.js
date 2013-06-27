/*
 *  Adds event listener to DOM element
 *
 *  Parameters:
 *    elem - DOM element for class to be added to
 *    type - string, name of event to listen for
 *    eventHandle - function, executed when event emitted
 *
 *  Example:
 *    addEvent(window, 'load', function(evt){
 *      console.log('window.onLoad');
 *    });
 */

var addEvent = function(elem, type, eventHandle) {
    if(elem === null || elem === undefined){
        return;
    }
    if(elem.addEventListener){
        elem.addEventListener(type, eventHandle, false);
    }else if(elem.attachEvent){
        elem.attachEvent('on' + type, eventHandle);
    }else{
        elem['on' + type] = eventHandle;
    }
};
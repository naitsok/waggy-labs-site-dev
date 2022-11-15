/**

 */
/**
 * Processes figure, table, listing, blockquote references before 
 * MathJax does the same for equations.
 * @param {DOM element} el - element which innerHTML needs processing
 */
function processRefs(el) {
    const classNames = ['blockquote', 'figure', 'listing', 'table'];
    for (let j in classNames) {
        var labelElements = document.getElementsByClassName('waggylabs-label-' + classNames[j]);
        for(var i = 0; i < labelElements.length; i++) {
            var label = labelElements[i].getAttribute('id');
            var regex = new RegExp('\\\\ref\{' + label + '\}', 'g');
            el.innerHTML = el.innerHTML.replace(regex, 
               `<span class="reference"><a href="#${label}">${i + 1}</a></span>`);
        }
    }
}
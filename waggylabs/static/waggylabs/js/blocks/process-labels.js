/**

 */
/**
 * Processes figure, table, listing, blockquote references before 
 * MathJax does the same for equations.
 * @param {string} ref - reference to be processed, e.g. \ref{...}
 */
function processRef(ref) {
    const classNames = ['blockquote', 'figure', 'listing', 'table'];
    for (let className in classNames) {
        var processedRef = processRef(ref, 'waggylabs-label-' + className);
        if (processRef) { return processedRef; }
    }
}

function processRef(ref, className) {
    var labelElements = document.getElementsByClassName(className);
    for(var i = 0; i < labelElements.length; i++) {
        var el = labelElements[i].getElementsByTagName('input')[0];
        if (el.value === ref) {
            return '<span class="MJX-TEX"><a href="#' + el.getAttribute('id') +'">('+
                (i + 1) + ')</a></span>';
        }
    }
}
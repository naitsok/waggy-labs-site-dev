/**

 */
/**
 * Processes figure, table, listing, blockquote references before 
 * MathJax does the same for equations.
 * @param {DOM element} el - element which innerHTML needs processing
 */
function processRefs(el) {
    const classNames = ['blockquote', 'embed', 'figure', 'listing', 'table'];
    for (let j in classNames) {
        var labelElements = document.getElementsByClassName('waggylabs-label-' + classNames[j]);
        for(var i = 0; i < labelElements.length; i++) {
            var label = labelElements[i].getAttribute('id');
            var regex = new RegExp('\\\\ref\{' + label + '\}', 'g');
            el.innerHTML = el.innerHTML.replace(regex, 
               `<span class="reference"><a href="#${label}">${i + 1}</a></span>`);
            // TODO: add correct class to the referenced elements for scrolling if navbar is fixed
        }
    }
}

function processCites(el) {
    var labelElements = document.getElementsByClassName('waggylabs-label-cite');
    var labelIds = []; // needed to collect the ids of the elements containing citations
    for (var i = 0; i < labelElements.length; i++) {
        labelElements[i].innerHTML = i + 1;
        labelIds.push(labelElements[i].id);
    }
    // var citeIds = []; // keeps the ids of for the current \cite{...}
    var re = /\\cite{(.*?)}/g;
    var matches = [];
    var citeHTMLs = [];
    var match;
    while (match = re.exec(el.innerHTML)) {
        var cites = match[1].split(","); // there can be more than one citation
        var citeIds = []; // keeps the ids of for the current \cite{...}
        for (let i in cites) {
            citeIds.push(labelIds.indexOf(cites[i]));
        }
        citeIds.sort();
        var citeHTML = "";
        for (let i in citeIds) {
            if (citeIds[i] === -1) {
                citeHTML = citeHTML + `<span class="reference"><a href="#">???</a></span>,`;
            }
            else {
                citeHTML = citeHTML + `<span class="reference"><a href="#${labelIds[citeIds[i]]}">${citeIds[i] + 1}</a></span>,`;
            }
        }
        matches.push(match[0]);
        citeHTMLs.push('[' + citeHTML.slice(0, -1) + ']');
    }
    for (let i in matches) {
        el.innerHTML = el.innerHTML.replace(matches[i], citeHTMLs[i]);
    }
}

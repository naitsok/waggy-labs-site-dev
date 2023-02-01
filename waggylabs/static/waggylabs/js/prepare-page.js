
/**
 * Processes figure, table, listing, blockquote references before 
 * MathJax does the same for equations.
 * @param {DOM element} element - element which innerHTML needs processing
 */
function prepareReferences(element) {
    const blockTypes = ['blockquote', 'embed', 'figure', 'listing', 'table'];
    blockTypes.forEach((blockType) => {
        const blockElements = element.getElementsByClassName('waggylabs-label-' + blockType);
        for(var i = 0; i < blockElements.length; i++) {
            // Add numbers to the elements if caption is present
            const blockLabelElem = blockElements[i].getElementsByClassName('waggylabs-entity-label')[0];
            if (blockLabelElem) {
                blockLabelElem.innerHTML = blockLabelElem.innerHTML + ' ' + String(i + 1) + '.';
            }
            // Replace \ref{...} blocks with numbers of corresponding blocks
            const regex = new RegExp('\\\\ref\{' + blockElements[i].id + '\}', 'g');
            element.innerHTML = element.innerHTML.replace(regex, 
               `<span class="reference"><a href="#${blockElements[i].id}">${i + 1}</a></span>`);
            // TODO: add correct class to the referenced elements for scrolling if navbar is fixed
        }
    });
}

/**
 * Processes literature citations and gererates references
 * @param {DOM element} element - element which innterHTML needs processing 
 */
function prepareCitations(element) {
    const labelIds = []; // needed to collect the ids of the elements containing citations
    element.querySelectorAll('.waggylabs-label-cite').forEach((citeElem, idx) => {
        citeElem.innerHTML = idx + 1;
        labelIds.push(citeElem.id);
    });
    const re = /\\cite{(.*?)}/g;
    const matches = [];
    const citeHTMLs = [];
    let match;
    while (match = re.exec(element.innerHTML)) {
        let citeIds = [];
        // there can be more than one citation
        let cites = match[1].split(','); 
        // keeps the ids of for the current \cite{...}
        cites.forEach((cite) => {
            citeIds.push(labelIds.indexOf(cite));
        });

        citeIds.sort();
        let citeHTML = '';
        citeIds.forEach((citeId) => {
            if (citeId === -1) {
                citeHTML = citeHTML + `<span class="reference"><a href="#">???</a></span>,`;
            }
            else {
                citeHTML = citeHTML + `<span class="reference"><a href="#${labelIds[citeId]}">${citeId + 1}</a></span>,`;
            }
        });

        matches.push(match[0]);
        citeHTMLs.push('[' + citeHTML.slice(0, -1) + ']');
    }
    matches.forEach((match, idx) => {
        element.innerHTML = element.innerHTML.replace(match, citeHTMLs[idx]);
    });
}

/**
 * Adds scroll-margin-top to anchor links for correct navbar position
 * @param {DOM element} element - element within which scroll-margin-top is updated
 */
function prepareScrollMarginTop(element) {
    const navbar = document.getElementById('navbar-header');
    let navbarHeight = '10px';
    if (navbar.classList.contains('sticky-top') || navbar.classList.contains('fixed-top')) {
        navbarHeight = String(navbar.offsetHeight + 10) + 'px';
    }
    // Add to MathJax labels
    element.querySelectorAll('mjx-labels').forEach((label) => {
        label.querySelectorAll('mjx-mtd').forEach((number) => {
            number.style.setProperty('scroll-margin-top', navbarHeight);
        });
    });
    // Other blocks winthin element
    const blockTypes = ['blockquote', 'embed', 'figure', 'listing', 'table', 'cite'];
    blockTypes.forEach((blockType) => {
        element.querySelectorAll('.waggylabs-label-' + blockType).forEach((blockElem) => {
            blockElem.style.setProperty('scroll-margin-top', navbarHeight);
        });
    });
}

/**
 * Prepares wisuals sidebar tab
 * @param {DOM element} element - - element within which blocks for sidebar will be processed
 */
function prepareSidebarVisuals(element) {
    // Citations are processed separately as they are in another sidebar tab
    // First process all types of blocks except equations
    const blockTypes = ['blockquote', 'embed', 'figure', 'listing', 'table'];
    blockTypes.forEach((blockType) => {
        element.querySelectorAll('.waggylabs-label-' + blockType).forEach((blockElem) => {
            const blockLabelElem = blockElem.querySelector('.waggylabs-entity-label');
            if (blockLabelElem) {
                // If label exists - update the labels in the sidebar blocks and modals
                const sb = document.getElementById('sb-' + blockLabelElem.id);
                const modal = document.getElementById('modal-' + blockLabelElem.id);
                if (sb) { sb.innerHTML = blockLabelElem.innerHTML; }
                if (modal) { modal.innerHTML = blockLabelElem.innerHTML; }
            }
        });
    });
    // Process equations
    element.querySelectorAll('.waggylabs-label-equation').forEach((eqElem) => {
        const eqLabelElem = eqElem.querySelector('.waggylabs-entity-label');
        if (eqLabelElem) {
            // If label exists - get the equation number generated by MathJax
            const numElem = eqElem.querySelector('mjx-labels').querySelector('mjx-mtext');
            if (numElem) {
                let eqNumber = '';
                // first and last children are opening and closing brackets, respectively
                for (let j = 1; j < numElem.children.length - 1; j++) {
                    eqNumber = eqNumber + numElem.children[j].classList[0].slice(-1);
                }
                if (eqNumber) {
                    eqLabelElem.innerHTML = eqLabelElem.innerHTML + ' ' + eqNumber + '.';
                }
            }
            const sb = document.getElementById('sb-' + eqLabelElem.id);
            const modal = document.getElementById('modal-' + eqLabelElem.id);
            if (sb) { sb.innerHTML = eqLabelElem.innerHTML; }
            if (modal) { modal.innerHTML = eqLabelElem.innerHTML; }
        }
    });
}

/**
 * Prepares sidebar table of contents
 * @param {DOM element} element - element from where to take headers
 */
function prepareSidebarContents(element) {
    const toc = document.getElementsByClassName('waggylabs-sidebar-toc')[0];
    const headerTags = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6'];
    const navbar = document.getElementById('navbar-header');
    var navbarHeight = '10px';
    if (navbar.classList.contains('sticky-top') || navbar.classList.contains('fixed-top')) {
        navbarHeight = String(navbar.offsetHeight + 10) + 'px';
    }
    if (toc) {
        element.childNodes.forEach((node, idx) => {
            if (headerTags.indexOf(node.tagName) >= 0) {
                node.setAttribute('id', 'waggylabs-header-' + String(idx));
                node.style.setProperty('scroll-margin-top', navbarHeight);
                var header_num = Number(node.tagName.slice(-1));
                var tocLink = document.createElement('a');
                tocLink.setAttribute('href', '#' + 'waggylabs-header-' + String(idx));
                tocLink.classList.add('nav-link', 'ms-2', 'ps-' + String(header_num - 1));
                tocLink.innerHTML = node.innerHTML;
                toc.appendChild(tocLink);
            }
        });
    }
}

function prepareSidebar(element) {
    prepareSidebarContents(element);
    prepareSidebarVisuals(element);
}
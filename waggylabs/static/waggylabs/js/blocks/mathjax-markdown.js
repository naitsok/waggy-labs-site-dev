/*
 * Copyright (c) 2022-present Konstantin Tamarov.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely. This software is provided 'as-is', without any express or implied
 * warranty.
 * 
 */

/*
 * Replaces standard EasyMDE markdown function to avoid parsing LaTeX 
 * math expressions according to the markdown rules.
 */

/**
 * Skip processing contents of \\(...\\) inline LaTeX equation, 
 * so that MathJax can render equations correctly.
 * @returns marked.js extenstion object
 */
function inlineMath() {
    return {
        name: 'inlineMath',
        level: 'inline',
        start(src) { src.indexOf('\\\\('); },
        tokenizer(src, tokens) {
            const match = src.match(/^\\\\\(+([^$\n]+?)\\\\\)+/);
            if (match) {
                return {
                    type: 'inlineMath',
                    raw: match[0],
                    text: match[1].trim()
                };
            }
        },
        renderer(token) {
            return token.raw.replace("\\\\(", "\\(").replace("\\\\)", "\\)");
        }
    };
}

/**
 * Skip processing contents of $...$ inline LaTeX equation, 
 * so that MathJax can render equations correctly.
 * @returns marked.js extenstion object
 */
function inlineMath2() {
    return {
        name: 'inlineMath2',
        level: 'inline',
        start(src) { return src.indexOf('$'); },
        tokenizer(src, tokens) {
            const match = src.match(/^\$+([^$\n]+?)\$+/);
            if (match) {
                return {
                    type: 'inlineMath2',
                    raw: match[0],
                    text: match[1].trim()
                };
            }
        },
        renderer(token) {
            // do not use $ for MathJax rendering to avoid collisions with $
            return token.raw.replace("$", "\\(").replace("$", "\\)");
        }
    };
}

/**
 * Skip processing contents of $$...$$ block LaTeX equation, so
 * that MathJax can render equations correctly.
 * @returns marked.js extenstion object
 */
function blockMath() {
    return {
        name: 'blockMath',
        level: 'block',
        start(src) { return src.indexOf('$$'); },
        tokenizer(src, tokens) {
            const match = src.match(/^\$\$+([^$]+?)\$\$+/);
            if (match) {
                return {
                    type: 'blockMath',
                    raw: match[0],
                    text: match[1].trim()
                };
            }
        },
        renderer(token) {
            return token.raw;
      }
    };
}

/**
 * Skip processing contents of \\[...\\] block LaTeX equation, so
 * that MathJax can render equations correctly.
 * @returns marked.js extenstion object
 */
function blockMath2() {
    return {
        name: 'blockMath',
        level: 'block',
        start(src) { return src.indexOf('\\\\['); },
        tokenizer(src, tokens) {
            const match = src.match(/^\\\\\[([^$]+?)\\\\\]/);
            if (match) {
                return {
                    type: 'blockMath',
                    raw: match[0],
                    text: match[1].trim()
                };
            }
        },
        renderer(token) {
            return token.raw.replace("\\\\[", "\\[").replace("\\\\]", "\\]");
        }
    };
}

/**
 * Skip processing contents of \begin{...}...\end{...} LaTeX equation, so
 * that MathJax can render equations correctly.
 * @returns marked.js extenstion object
 */
function beginMath() {
    return {
      name: 'beginMath',
      level: 'block',
      start(src) {  return src.indexOf('\\begin{'); },
      tokenizer(src, tokens) {
        const match = src.match(/^\\begin{(.*?)}([\s\S]*?)\\end{\1}/);
        if (match) {
          return {
            type: 'beginMath',
            raw: match[0],
            text: match[1].trim()
          };
        }
      },
      renderer(token) {
        return token.raw;
      }
    };
}

/**
 * Processes figure, table, listing, blockquote labels before 
 * MathJax does the same for equations.
 * @returns marked.js extension object
 */
function refLabel() {
    return {
        name: 'refLabel',
        level: 'inline',
        start(src) {return src.indexOf('\\ref{'); },
        tokenizer(src, tokens) {
            const match = src.match(/^\\ref{(.*?)}/);
            if (match) {
                return {
                    type: 'refLabel',
                    raw: match[0],
                    text: match[1]
                }
            }
        },
        renderer(token) {
            var processedRef = processRef(token.text);
            if (processedRef) {
                return processedRef;
            }
            else {
                return token.raw;
            }
        }
    }
}

/**
 * Processes figure, table, listing, blockquote labels before 
 * MathJax does the same for equations.
 * @returns marked.js extension object
 */
function citeLabel() {
    return {
        name: 'citeLabel',
        level: 'inline',
        start(src) {return src.indexOf('\\cite{'); },
        tokenizer(src, tokens) {
            const match = src.match(/^\\cite{(.*?)}/);
            if (match) {
                return {
                    type: 'citeLabel',
                    raw: match[0],
                    text: match[1]
                }
            }
        },
        renderer(token) {
            var processedCite = processCite(token.text);
            if (processedCite) {
                return '[' + processedCite + ']';
            }
            else {
                return '[???]';
            }
        }
    }
}

/**
 * Processes figure, table, listing, blockquote references before 
 * MathJax does the same for equations.
 * @param {string} ref - reference to be processed, e.g. content inside curly brackets of \ref{...}
 * ref can contain only one reference to the certain type of an item to be referenced
 * @returns - span element if the reference id was found or undefined if not
 */
 function processRef(ref) {
    const refTypes = ['blockquote', 'figure', 'listing', 'table', 'embed'];
    for (let i in refTypes) {
        var processedRef = processRefbyType(ref, refTypes[i]);
        if (processedRef) { return processedRef; }
    }
}

/**
 * Processes one ref by one type
 * @param {string} ref - reference to be processed, e.g. content inside curly brackets of  \ref{...}
 * @param {string} refType - type of reference to be processed: ['blockquote', 'figure', 'listing', 'table', 'embed']
 * @returns - span element if the reference id was found or undefined if not
 */
function processRefbyType(ref, refType) {
    var labelElements = document.getElementsByClassName('waggylabs-label-' + refType);
    // there can be several refs separated by comma, then we need to collect their
    // numbers and if needed make them in order of appearance
    // var refs =  ref.split(",");
    // var labelIds = [];
    for(var i = 0; i < labelElements.length; i++) {
        var el = labelElements[i].getElementsByTagName('input')[0];
        if (el.value === ref) {
            return `<span class="reference"><a href="#${el.getAttribute('id')}">${i + 1}</a></span>`;
        }
    }
}

/**
 * Processes citations from \cite{...} block
 * @param {string} cite - inner text inside the curly brackets
 * @returns - HTML string with links to the literature
 */
function processCite(cite) {
    var labelElements = document.getElementsByClassName('waggylabs-label-cite');
    var labelIds = []; // needed to collect the ids of the elements containing citations
    var labelVals = []; // needed to collect values that define citations
    for (var i = 0; i < labelElements.length; i++) {
        var el = labelElements[i].getElementsByTagName('input')[0];
        labelIds.push(el.id);
        labelVals.push(el.value);
    }
    var cites = cite.split(","); // there can be more than one citation
    var citeIds = []; // keeps the ids of for the current \cite{...}
    for (let i in cites) {
        citeIds.push(labelVals.indexOf(cites[i]));
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
    return citeHTML.slice(0, -1);
}

var anchorToExternalRegex = new RegExp(/(<a.*?https?:\/\/.*?[^a]>)+?/g);

/**
 * Modify HTML to add 'target="_blank"' to links so they open in new tabs by default. Same as in EasyMDE.
 * @param {string} htmlText - HTML to be modified.
 * @return {string} The modified HTML text.
 */
function addAnchorTargetBlank(htmlText) {
    var match;
    while ((match = anchorToExternalRegex.exec(htmlText)) !== null) {
        // With only one capture group in the RegExp, we can safely take the first index from the match.
        var linkString = match[0];

        if (linkString.indexOf('target=') === -1) {
            var fixedLinkString = linkString.replace(/>$/, ' target="_blank">');
            htmlText = htmlText.replace(linkString, fixedLinkString);
        }
    }
    return htmlText;
}

/**
 * Modify HTML to remove the list-style when rendering checkboxes. Same as in EasyMDE.
 * @param {string} htmlText - HTML to be modified.
 * @return {string} The modified HTML text.
 */
function removeListStyleWhenCheckbox(htmlText) {

    var parser = new DOMParser();
    var htmlDoc = parser.parseFromString(htmlText, 'text/html');
    var listItems = htmlDoc.getElementsByTagName('li');

    for (var i = 0; i < listItems.length; i++) {
        var listItem = listItems[i];

        for (var j = 0; j < listItem.children.length; j++) {
            var listItemChild = listItem.children[j];

            if (listItemChild instanceof HTMLInputElement && listItemChild.type === 'checkbox') {
                // From Github: margin: 0 .2em .25em -1.6em;
                listItem.style.marginLeft = '-1.5em';
                listItem.style.listStyleType = 'none';
            }
        }
    }

    return htmlDoc.documentElement.innerHTML;
}

/**
 * Modify HTML to remove the list-style when rendering checkboxes. Same as in EasyMDE.
 * @param {string} text - raw text from the EasyMDE
 * @param {EasyMDE} mde - EasyMDE object
 * @return {string} The modified HTML text.
*/
function mathjaxMarkdown(text, mde) {
    var easymdeOptions = {};
    if (mde) { easymdeOptions = mde.options; }
    // First check if the editor is in LaTeX or not, it means that we are in the Equation block.
    // Then \begin{equation} and \label{...} needs to be added if they are absent
    if (easymdeOptions && easymdeOptions.overlayMode && !easymdeOptions.overlayMode.combine) {
        text = text.trim().replace(/^\$+|\$+$/, '');
        // add \begin{equation}, \end{equation} if not present
        if (text.search(/\\begin\{/i) === -1) {
            text = "\\begin{equation}\n" + text + "\\end{equation}";
        }
        if (text.search(/\\label\{/i) === -1) {
            // label not found, we have to add it from the neighbour Label block
            const label = mde.element.closest(".struct-block").getElementsByTagName("input")[0];
            if (label.value) {
                const idx = text.search(/\\end\{/i);
                text = text.slice(0, idx) + "\\label{" + label.value + "}\n" + text.slice(idx);
            }
        }
    }

    /* Similar to EasyMDE markdown(text) function but with addtional makedjs extensions */
    if (marked) {
        // Initialize
        var markedOptions;
        if (easymdeOptions && easymdeOptions.renderingConfig && easymdeOptions.renderingConfig.markedOptions) {
            markedOptions = easymdeOptions.renderingConfig.markedOptions;
        } else {
            markedOptions = {};
        }

        // Update options
        if (easymdeOptions && easymdeOptions.renderingConfig && easymdeOptions.renderingConfig.singleLineBreaks === false) {
            markedOptions.breaks = false;
        } else {
            markedOptions.breaks = true;
        }

        if (easymdeOptions && easymdeOptions.renderingConfig && easymdeOptions.renderingConfig.codeSyntaxHighlighting === true) {

            /* Get HLJS from config or window */
            var hljs = easymdeOptions.renderingConfig.hljs || window.hljs;

            /* Check if HLJS loaded */
            if (hljs) {
                markedOptions.highlight = function (code, language) {
                    if (language && hljs.getLanguage(language)) {
                        return hljs.highlight(language, code).value;
                    } else {
                        return hljs.highlightAuto(code).value;
                    }
                };
            }
        }

        // Replace \$ signs in order to avoid collisions with $...$ equations processing
        text = text.replace(/\\\$/g, "{{DOLLAR}}");

        // Set options
        marked.setOptions(markedOptions);

        // Set extensions
        marked.use({ extensions: [inlineMath(), inlineMath2(), blockMath(), blockMath2(), beginMath(), refLabel(), citeLabel()] });

        // Convert the markdown to HTML
        var htmlText = marked.parse(text);

        // Replace $ back after parsing (there $...$ is replaced to \\(...\\))
        htmlText = htmlText.replace(/{{DOLLAR}}/g, "$");

        // Sanitize HTML
        if (easymdeOptions && easymdeOptions.renderingConfig && typeof easymdeOptions.renderingConfig.sanitizerFunction === 'function') {
            htmlText = easymdeOptions.renderingConfig.sanitizerFunction.call(this, htmlText);
        }

        // Edit the HTML anchors to add 'target="_blank"' by default.
        htmlText = addAnchorTargetBlank(htmlText);

        // Remove list-style when rendering checkboxes
        htmlText = removeListStyleWhenCheckbox(htmlText);

        return htmlText;
    }
}
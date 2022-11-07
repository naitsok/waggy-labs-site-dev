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
 * Replaces standard EasyMDE markdown function to avoid parsing LaTeX math expressions according to the markdown rules.
 */

function inlineMath() {
    return {
        name: 'inlineMath',
        level: 'inline',
        start(src) { src.indexOf('\\\\('); }, // return src.indexOf('$'); }, // 
        tokenizer(src, tokens) {
            const match = src.match(/^\\\\\(+([^$\n]+?)\\\\\)+/); // src.match(/^\$+([^$\n]+?)\$+/); //
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
 * @param {object} easymdeOptions - EasyMDE options object
 * @return {string} The modified HTML text.
*/
function mathjaxMarkdown(text, easymdeOptions) {
    // First check if the editor is in LaTeX or not, then \begin{equation} needs to be added if it is absent
    if (!easymdeOptions.overlayMode.combine) {
        if (!text.trim().startsWith("\\begin{")) {
            text = "\\begin{equation}\n" + text.trim().replace(/^\$+|\$+$/gm,'') + "\n\\end{equation}";
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

        // Set options
        marked.setOptions(markedOptions);

        // Set extensions
        // marked.use(blockMath());
        marked.use({ extensions: [inlineMath(), blockMath(), blockMath2(), beginMath()] });

        // Convert the markdown to HTML
        var htmlText = marked.parse(text);

        // Sanitize HTML
        if (easymdeOptions.renderingConfig && typeof easymdeOptions.renderingConfig.sanitizerFunction === 'function') {
            htmlText = easymdeOptions.renderingConfig.sanitizerFunction.call(this, htmlText);
        }

        // Edit the HTML anchors to add 'target="_blank"' by default.
        htmlText = addAnchorTargetBlank(htmlText);

        // Remove list-style when rendering checkboxes
        htmlText = removeListStyleWhenCheckbox(htmlText);

        return htmlText;
    }
}
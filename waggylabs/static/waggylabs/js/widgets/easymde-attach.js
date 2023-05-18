/*
 * vim:sw=4 ts=4 et:
 * Copyright (c) 2015-present Torchbox Ltd.
 * hello@torchbox.com
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely. This software is provided 'as-is', without any express or implied
 * warranty.
 * 
 * Updated by Konstantin Tamarov for Waggy Labs to typeset MathJax.
 */

/*
 * Used to initialize Easy MDE when Markdown blocks are used in StreamFields
 */

/**
 * Gets Font Awesome icon for EasyMDE math buttons
 * @param {string} pattern - math pattern
 * @returns CSS class for the Font Awesome icon, free version has only subscript and superscript icons
 */
function getIcon(pattern) {
    switch (pattern) {
        case "subscript": return "fa fa-subscript";
        case "superscript": return "fa fa-superscript";
        default: return undefined;
    }
}

/**
 * Gets text value for EasyMDE math button when no Icon available
 * @param {string} pattern - math pattern
 * @returns Text for button because there are no suitable Font Awesome Icons
 */
function getText(pattern) {
    switch (pattern) {
        case "equation": return "{Eq}";
        case "matrix": return "[M]";
        case "align": return "{Al}";
        case "split": return "{Sp}";
        case "multiline": return "{Mu}";
        case "gather": return "{Ga}";
        case "alignat": return "{At}";
        case "flalign": return "{Fl}";
        default: return undefined;
    }
}

/**
 * @param {string} toolbarConfig - the configuration string with toolbar buttons, such as
 *  "bold,italic,strikethrough,|,unordered-list,ordered-list,link,|,preview,side-by-side,fullscreen,guide"
 * @returns toolbar and shortcuts for EasyMDE
 */
function createToolbar(toolbarConfig) {
    if (toolbarConfig === 'false') {
        return false;
    }
    // Math patterns from the AMS Math LaTeX package
    var allMathPatterns = ["subscript", "superscript", "equation", "matrix", "split", "multiline", "gather", "align", "alignat", "flalign"];
    // Shortcuts for the math patterns
    var allShortcuts = {
        "subscript": "Cmd--",
        "superscript": "Cmd-=",
        "equation": "Cmd-Alt-E",
        "matrix": "Cmd-Alt-M",
        "split": "Cmd-Alt-S",
        "multiline": "Cmd-Alt-U",
        "gather": "Cmd-Alt-G",
        "align": "Cmd-Alt-A",
        "alignat": "Cmd-Alt-T",
        "flalign": "Cmd-Alt-F"
    }
    
    // create math button function
    const createMathButton = (pattern) => {
        return {
            name: pattern.toLowerCase(),
            action: (editor) => {
                var doc = editor.element.codemirror.getDoc();
                var startCursor = doc.getCursor("from");
                var endCursor = doc.getCursor("to");
                var selection = doc.getSelection();
                var data = "";

                if (pattern === "superscript" || pattern === "subscript") {
                    if (selection.length !== 0) {
                        data = "\\text{" + selection + "}"; 
                    }
                    data = (pattern === "subscript") ? "$"+ data + "_{}$" : "$"+ data + "^{}$";
                    doc.replaceRange(data, startCursor, endCursor);
                    doc.setCursor(startCursor.line, startCursor.ch + data.length - 2);
                }
                else {
                    var addLine = 0;
                    if (selection.length === 0) {
                        data = "\\begin{" + pattern + "}\n\n\\end{" + pattern + "}\n";
                    }
                    else {
                        data = "\\begin{" + pattern + "}\n" + selection + "\n\\end{" + pattern + "}\n";
                    }
                    // check if the beginning of selection is at the beginning of line or not
                    if (startCursor.ch !== 0) {
                        data = "\n" + data;
                        addLine = 1;
                    }
                    doc.replaceRange(data, startCursor, endCursor);
                    // Put the cursor at the new position withing the \begin{...} block
                    var selectedLines = selection.split("\n");
                    doc.setCursor({
                        line: startCursor.line + addLine + selectedLines.length,
                        ch: selectedLines[selectedLines.length - 1].length
                    });
                }
                editor.element.codemirror.focus();
            },
            className: getIcon(pattern),
            text: getText(pattern),
            title: pattern.charAt(0).toUpperCase() + pattern.slice(1)
        }
    }

    // First prepare menu if there is "equation", "matrix", "align", etc. present in the toolbar settings
    var toolbar = [];
    var shortcuts = {};
    var toolbarButtons = toolbarConfig.split(",");
    for (let i = 0; i < toolbarButtons.length; i++) {
        if (allMathPatterns.indexOf(toolbarButtons[i]) >= 0) {
            toolbar.push(createMathButton(toolbarButtons[i]));
            shortcuts[toolbarButtons[i]] = allShortcuts[toolbarButtons[i]];
        } else if (toolbarButtons[i] === "preview") {
            toolbar.push({
                name: "preview",
                action: togglePreviewAll,
                className: "fa fa-eye",
                noDisable: true,
                title: "Toggle Preview",
                default: true,
            });
            shortcuts[toolbarButtons[i]] = "Cmd-P";
        } else if (toolbarButtons[i] === "side-by-side") {
            toolbar.push({
                name: "side-by-side",
                action: toggleSideBySide,
                className: "fa fa-columns",
                noDisable: true,
                noMobile: true,
                title: "Toggle Side by Side",
                default: true,
            });
            shortcuts[toolbarButtons[i]] = "F9";
        } else if (toolbarButtons[i] === "fullscreen") {
            toolbar.push({
                name: "fullscreen",
                action: toggleFullScreen,
                className: "fa fa-arrows-alt",
                noDisable: true,
                noMobile: true,
                title: "Toggle Fullscreen",
                default: true,
            });
            shortcuts[toolbarButtons[i]] = "F11";
        } else {
            toolbar.push(toolbarButtons[i]);
        }
    }
    // Finally add autocomplete hidden button
    toolbar.push({
        name: "autocomplete",
        className: "d-none",
        noDisable: true,
        noMobile: true,
        title: "Autocomplete",
        default: true,
        action: (editor) => CodeMirror.showHint(
            editor.codemirror,
            getHinter(),
        ),
    });
    shortcuts["autocomplete"] = "Cmd-Space";
    return [toolbar, shortcuts];
}

function getHinter() {
    const suggestionList = ['list1', 'list2', 'list3'];
    return function hintFunction(cm) {
        const cur = cm.getCursor();
        const token = cm.getTokenAt(cur);
        const { start, end } = token;

        const from = CodeMirror.Pos(cur.line, start);
        const to = CodeMirror.Pos(cur.line, end);

        // const allResults = { from, to, list: suggestionList.map((s) => s.path) };

        // const currentLine = cm.getRange({ line: from.line, ch: 0 }, to);

        // const lastSeparatedWord = /\b(\w+)$/g;
        // const allMatches = [...currentLine.matchAll(lastSeparatedWord)];

        // if (!allMatches.length) {
        //     return allResults;
        // }

        const matchedWord = suggestionList[0];
        // const word = matchedWord[0];

        // if (!word) {
        //     return allResults;
        // }

        const suggestions = suggestionList;

        return {
            from: {
                // Current line
                line: from.line,

                // Position of the matched
                ch: from.ch, //matchedWord.index !== undefined ? matchedWord.index : 
            },
            to,
            list: suggestions,
        }
    }
}

/**
 * @param {string} statusConfig - true for default status bar, fals for no bar,
 * list of comma separated values for custom toolbar
 * @returns - configuration of the status bar
 */
function createStatusBar(statusConfig){
    if (statusConfig === "false") {
        return false;
    }
    if (statusConfig === "true") {
        return ['autosave', 'lines', 'words', 'cursor'];
    }
    return statusConfig.split(",");
}

/**
 * Updates the text value of the EasyMDE if it is used for equation blocks. Updating
 * is needed to add \begin{equation} and \label{...} commands if they are absent.
 * @param {*} text - value of EasyMDE, i.e. EasyMDE.value()
 * @param {*} mde - instance of EasyMDE Editor
 * @returns - updated text with necessary commands
 */
function updateTextIfEquation(text, mde) {
    // Check if the editor is in LaTeX or not, it means that we are in the Equation block.
    // Then \begin{equation} and \label{...} needs to be added if they are absent
    if (mde && mde.options && mde.options.overlayMode && !mde.options.overlayMode.combine) {
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

    return text;
}

/**
 * Toggles side-by-side mode with correct handling of other EasyMDEs
 * on the page to correctly render MathJax equations.
 * @param {EaseMDE} editor - EasyMDE object
 */
function toggleSideBySide(editor) {
    // We need to keep other editors in preview mode
    // in order to correctly render MathJax refs in the
    // side by side mode
    if (!editor.isSideBySideActive()) {
        // Collects all the EasyMDE (except this one in side-by-side mode) data in order
        // to re-render markdown content and re-typeset MathJax
        // Needed to speed up typesetting and do not care about other content and EasyMDEs
        // on the page
        var wrapper = editor.codemirror.getWrapperElement();
        window.allMarkdown = '';
        var textAreas = document.getElementsByTagName("textarea");
        for (let i in textAreas) {
            if(textAreas[i].easyMDE && textAreas[i].easyMDE.element.id !== editor.element.id) {
                // now check if the EasyMDE contain equation, i.e. it is in only in the TeX mode
                window.allMarkdown = window.allMarkdown + updateTextIfEquation(textAreas[i].easyMDE.value(), textAreas[i].easyMDE);
            }
        }

        var allMarkdownElem = wrapper.querySelector('.waggylabs-all-markdown');
        if (!allMarkdownElem) {
            allMarkdownElem = document.createElement('div');
            allMarkdownElem.classList.add('waggylabs-all-markdown');
            allMarkdownElem.style.display = 'none';
            wrapper.insertBefore(allMarkdownElem, wrapper.lastChild);
        }
        allMarkdownElem.innerHTML = editor.options.previewRender(window.allMarkdown, editor);
        // store the necesarry values for the interval check and update of markdown and MathJax
        window.allMarkdownElem = allMarkdownElem;
        window.easyMDE = editor;
        window.mathJaxTimer = setInterval(resetMathJax, 1000);
    } else {
        clearInterval(window.mathJaxTimer);
    }
    // Actually go to side-by-side mode
    EasyMDE.toggleSideBySide(editor);
}

function toggleFullScreen(editor) {
    if (window.mathJaxTimer) {
        clearInterval(window.mathJaxTimer);
    }
    EasyMDE.toggleFullScreen(editor);
}

/**
 * Toggles preview mode for the specified editor
 * @param {EasyMDE} editor - EasyMDE editor object
 * @param {boolean} isPreview - the preview mode to set for the editor
 */
function togglePreview(editor, isPreview) {
    var cm = editor.codemirror;
    var wrapper = cm.getWrapperElement();
    var toolbar_div = editor.toolbar_div;
    var toolbar = editor.options.toolbar ? editor.toolbarElements.preview : false;
    var preview = wrapper.lastChild;

    // Turn off side by side if needed
    var sidebyside = cm.getWrapperElement().nextSibling;
    if (sidebyside.classList.contains('editor-preview-active-side'))
        EasyMDE.toggleSideBySide(editor);

    if (!preview || !preview.classList.contains('editor-preview-full')) {

        preview = document.createElement('div');
        preview.className = 'editor-preview-full';

        if (editor.options.previewClass) {

            if (Array.isArray(editor.options.previewClass)) {
                for (var i = 0; i < editor.options.previewClass.length; i++) {
                    preview.classList.add(editor.options.previewClass[i]);
                }

            } else if (typeof editor.options.previewClass === 'string') {
                preview.classList.add(editor.options.previewClass);
            }
        }

        wrapper.appendChild(preview);
    }

    var editorPreviewMode = preview.classList.contains('editor-preview-active');

    if (editorPreviewMode !== isPreview) {
        // Editor is not in the same preview state as others, 
        // preview mode must be changed
        if (editorPreviewMode) {
            preview.classList.remove('editor-preview-active');
            if (toolbar) {
                toolbar.classList.remove('active');
                toolbar_div.classList.remove('disabled-for-preview');
            }
        } else {
            // When the preview button is clicked for the first time,
            // give some time for the transition from editor.css to fire and the view to slide from right to left,
            // instead of just appearing.
            setTimeout(() => {
                preview.classList.add('editor-preview-active');
            }, 1);
            if (toolbar) {
                toolbar.classList.add('active');
                toolbar_div.classList.add('disabled-for-preview');
            }
        }
    }

    var preview_result = editor.options.previewRender(editor.value(), preview);
    if (preview_result !== null) {
        preview.innerHTML = preview_result;
    }
}

/**
 * Toggles the preview mode of all the EasyMDE editors
 * on the page depending on the preview mode of this 
 * editor (editor that toggled preview mode)
 * @param {EasyMDE} editor -  EasyMDE editor object
 * @param {boolean} isPreview - if present, forces the specified preview mode
 * @param {boolean} skipMathJax - when going into side-by-side mode MathJax
 * typeset is not needed right after going into preview mode; it is needed
 * only after going into side-by-side mode.
 */
function togglePreviewAll(editor, isPreview, skipMathJax) {
    if (window.mathJaxTimer) {
        clearInterval(window.mathJaxTimer);
    }

    if (isPreview === undefined) {
        isPreview = !editor.isPreviewActive();
    }
    var textAreas = document.getElementsByTagName("textarea");
    for (let i in textAreas) {
        if(textAreas[i].easyMDE) {
            togglePreview(textAreas[i].easyMDE, isPreview);
        }
    }
    if (isPreview && skipMathJax === undefined) {
        // var preview = editor.codemirror.getWrapperElement().lastChild;
        MathJax.typesetClear();
        MathJax.texReset();
        MathJax.typeset([document.getElementById("main")]);
    }
}

/**
 * Resets MathJax to correctly display equation numbers during side-by-side editing
 * @param {EasyMDE} editor - EasyMDE object
 */
function resetMathJax() {
    if (window.allMarkdown && window.allMarkdownElem && window.easyMDE) {
        window.allMarkdownElem.innerHTML = renderMarkdown(window.allMarkdown, window.easyMDE);
        MathJax.typesetClear();
        MathJax.texReset();
        MathJax.typeset([window.allMarkdownElem, window.easyMDE.gui.sideBySide]);
    }
    
}

function easymdeAttach(id) {
    var textArea = document.getElementById(id);
    var toolbar = undefined;
    var shortcuts = undefined;
    if (textArea.getAttribute("easymde-toolbar")) {
        [toolbar, shortcuts] = createToolbar(textArea.getAttribute("easymde-toolbar"));
    } 

    var mde = new EasyMDE({
        element: textArea,
        autofocus: false,
        autoDownloadFontAwesome: true, // autoDownloadFontAwesome,
        lineNumbers: true,
        minHeight: textArea.getAttribute("easymde-min-height") || undefined,
        maxHeight: textArea.getAttribute("easymde-max-height") || undefined,
        overlayMode: {
            mode: CodeMirror.getMode({}, "stex"),
            combine: textArea.getAttribute("easymde-combine").toLowerCase() === "true",
        },
        renderingConfig: {
            codeSyntaxHighlighting: true,
        },
        spellChecker: false,
        showIcons: (textArea.getAttribute("easymde-toolbar")) ? undefined : ["strikethrough", "code", "table"],
        toolbar: (textArea.getAttribute("easymde-toolbar")) ? toolbar : undefined,
        shortcuts: (textArea.getAttribute("easymde-toolbar")) ? shortcuts : undefined,
        status: createStatusBar(textArea.getAttribute("easymde-status")),
        unorderedListStyle: "-",
    });
    
    mde.options.previewRender = (plainText, preview) => {
        // if (mde.isSideBySideActive()) {
        //     setTimeout(() => {
        //         resetMathJax(mde);
        //     }, 1000);
        // }
        return renderMarkdown(plainText, mde);
    };
    mde.render();

    // Save the codemirror instance on the original html element for later use.
    mde.element.codemirror = mde.codemirror;

    mde.codemirror.on("change", () => {
        document.getElementById(id).value = mde.value();
    });

    // Attach the mde object to the text area.
    // It is needed for the new togglePreview function,
    // which toggles preview of all the EasyMDEs on the page.
    // It is in turn needed for correct rendering of MathJax
    // equation references.
    textArea.easyMDE = mde;
}

/*
* Used to initialize content when MarkdownFields are used in admin panels.
*/
function refreshCodeMirror(e) {
    setTimeout(() => {
            e.CodeMirror.refresh();
            e.CodeMirror.focus();
        }, 200
    );
}

// Wagtail < 3.0
document.addEventListener('shown.bs.tab', () => {
    document.querySelectorAll('.CodeMirror').forEach((e) => {
        refreshCodeMirror(e);
    });
});

// Wagtail >= 3.0
document.addEventListener('wagtail:tab-changed', () => {
    document.querySelectorAll('.CodeMirror').forEach((e) => {
        refreshCodeMirror(e);
    });
});
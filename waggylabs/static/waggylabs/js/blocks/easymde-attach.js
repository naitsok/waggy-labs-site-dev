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
        } else {
            toolbar.push(toolbarButtons[i]);
        }
    }
    return [toolbar, shortcuts];
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
 * Toggles side-by-side mode with correct handling of other EasyMDEs
 * on the page to correctly render MathJax equations.
 * @param {EaseMDE} editor - EasyMDE object
 */
function toggleSideBySide(editor) {
    // We need to keep other editors in preview mode
    // in order to correctly render MathJax refs in the
    // side by side mode
    if (!editor.isSideBySideActive() && !editor.isFullscreenActive()) {
        togglePreviewAll(editor, true);
        // EasyMDE.togglePreview(editor);
    } else {
        resetPreviewAll(editor);
    }
    //EasyMDE.togglePreview(editor);
    // Timeout is needed beacuse there is timeout in togglePreview functions.
    // Without this timeout, toggleSideBySite will happen earlier than
    // togglePreviewAll finishes.
    setTimeout(function() {
        EasyMDE.toggleSideBySide(editor);
        setTimeout(function() {
            resetPreviewAll(editor);
        }, 10);
    }, 50);
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
            setTimeout(function () {
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
        MathJax.texReset();
        MathJax.typesetClear([document.getElementById("main")]);
        MathJax.typeset([document.getElementById("main")]);
    }
}

/**
 * Resets all the other EasyMDEs on the page for correct MathJax processing
 * @param {EasyMDE} editor - EasyMDE object
 */
function resetPreviewAll(editor) {
    var textAreas = document.getElementsByTagName("textarea");
    for (let i in textAreas) {
        if(textAreas[i].easyMDE && textAreas[i].easyMDE.element.id !== editor.element.id) {
            var preview = textAreas[i].easyMDE.codemirror.getWrapperElement().lastChild;
            preview.innerHTML = mathjaxMarkdown(textAreas[i].easyMDE.value(), textAreas[i].easyMDE);
        }
    }
    MathJax.texReset();
    MathJax.typesetClear([document.getElementById("main")]);
    MathJax.typeset([document.getElementById("main")]);
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
        if (mde.isSideBySideActive()) {
            setTimeout(() => {
                resetPreviewAll(mde);
            }, 500);
        }
        return mathjaxMarkdown(plainText, mde);
    };
    mde.render();

    // Save the codemirror instance on the original html element for later use.
    mde.element.codemirror = mde.codemirror;

    mde.codemirror.on("change", function() {
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
    setTimeout(
        function() {
            e.CodeMirror.refresh();
            e.CodeMirror.focus();
        }, 200
    );
}

// Wagtail < 3.0
document.addEventListener('shown.bs.tab', function() {
    document.querySelectorAll('.CodeMirror').forEach(function(e) {
        refreshCodeMirror(e);
    });
});

// Wagtail >= 3.0
document.addEventListener('wagtail:tab-changed', function() {
    document.querySelectorAll('.CodeMirror').forEach(function(e) {
        refreshCodeMirror(e);
    });
});
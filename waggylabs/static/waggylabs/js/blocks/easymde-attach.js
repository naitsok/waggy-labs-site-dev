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
        }
        else {
            toolbar.push(toolbarButtons[i]);
        }
    }
    return [toolbar, shortcuts];
}

/**
 * 
 * @param {string} statusConfig - true for default status bar, fals for no bar,
 * list of comma separated values for custom toolbar
 * 
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
    
    mde.options.previewRender = (plainText) => {
        setTimeout(() => {
            var wrapper = mde.codemirror.getWrapperElement();
            var preview = wrapper.nextSibling;
            if (!preview.classList.contains('editor-preview-active-side')) {
                preview = wrapper.lastChild;
            }
            MathJax.texReset();
            MathJax.typesetClear([preview]);
            MathJax.typeset([preview]);
        }, 500);
        return mathjaxMarkdown(plainText, mde.options);
    };
    mde.render();

    // Save the codemirror instance on the original html element for later use.
    mde.element.codemirror = mde.codemirror;

    mde.codemirror.on("change", function() {
        document.getElementById(id).value = mde.value();
    });
}

/*
* Used to initialize content when MarkdownFields are used in admin panels.
*/
function refreshCodeMirror(e) {
    setTimeout(
        function() {
            e.CodeMirror.refresh();
        }, 100
    );
}

// Wagtail < 3.0
document.addEventListener('shown.bs.tab', function() {
    document.querySelectorAll('.CodeMirror').forEach(function(e) {
        refreshCodeMirror(e)
    });
});

// Wagtail >= 3.0
document.addEventListener('wagtail:tab-changed', function() {
    document.querySelectorAll('.CodeMirror').forEach(function(e) {
        refreshCodeMirror(e)
    });
});
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
function easymdeAttach(id) { //, autoDownloadFontAwesome) {

    var textArea = document.getElementById(id);
    var mde = new EasyMDE({
        element: textArea,
        autofocus: false,
        autoDownloadFontAwesome: true, // autoDownloadFontAwesome,
        lineNumbers: true,
        minHeight: textArea.getAttribute("easymde-min-height") || undefined,
        maxHeight: textArea.getAttribute("easymde-max-height") || undefined,
        overlayMode: {
            mode: CodeMirror.getMode({}, "stex"),
            combine: true,
        },
        renderingConfig: {
            codeSyntaxHighlighting: true,
        },
        spellChecker: false,
        showIcons: (textArea.getAttribute("easymde-toolbar")) ? undefined : ["strikethrough", "code", "table"],
        toolbar: (textArea.getAttribute("easymde-toolbar")) ? textArea.getAttribute("easymde-toolbar").split(",") : undefined,
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
        return mde.markdown(plainText);
    };
    mde.render();

    // Save the codemirror instance on the original html element for later use.
    mde.element.codemirror = mde.codemirror;
    // mde.codemirror.setOption("mode", "python");

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
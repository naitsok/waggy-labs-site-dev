class EquationBlockDefinition extends window.wagtailStreamField.blocks.StructBlockDefinition {
    render(placeholder, prefix, initialState, initialError) {
        const block = super.render(
            placeholder,
            prefix,
            initialState,
            initialError,
        );

        const equationField = document.getElementById(prefix + "-equation");
        const previewDiv = document.createElement("div");
        equationField.parentNode.insertBefore(previewDiv, equationField.nextSibling);
        var cm = CodeMirror.fromTextArea(equationField, {
            value: equationField.value,
            mode: "stex",
            lineNumbers: true,
            styleActiveLine: true,
            matchBrackets: true
        });
        cm.on("change", function() {
            cm.save();
            var cmValue = cm.getValue().toLowerCase();
            if (cmValue.startsWith("\\begin") || cmValue.startsWith("$$")) {
                previewDiv.innerHTML(m.getValue());
            }
            else {
                previewDiv.innerHTML("\\begin{equation}" + cm.getValue() + "\\end{equation}");
            }

            MathJax.texReset();
            MathJax.typesetClear([previewDiv]);
            MathJax.typeset([previewDiv]);
        });

        return block;
    }
}
window.telepath.register('waggy_labs.blocks.EquationBlock', EquationBlockDefinition);
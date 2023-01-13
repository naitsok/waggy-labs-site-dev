
(() => {
    function createColorWidgets() {
        var elements = document.querySelectorAll('input.waggylabs-color-input');

        for (let i = 0; i < elements.length; i++) {
            colorAttach(elements[i].id);
        }
    }

    window.addEventListener("DOMContentLoaded", () => {
        // Check we are not inside a StreamField - then icon-input-adapter.js inits the autocompletes
        if (document.querySelector("[data-streamfield-stream-container]") === null) {
            createColorWidgets();
            let observer = new MutationObserver(() => {
                setTimeout(() => { 
                    createColorWidgets(); 
                }, 50);
            });
            observer.observe(document.getElementById("main"), { 
                childList: true,
                subtree: true, 
            });
        }
    });
})();


/**
 * Attaches the color and opacity input elements to the hidden input associates with the\
 * database field
 */
function colorAttach(id) {

    const hidden = document.getElementById(id);
    if (!hidden.classList.contains('ui-color')) {
        const text = document.getElementById('text_' + hidden.name);
        const color = document.getElementById('color_' + hidden.name);
        const number = document.getElementById('number_' + hidden.name);
        const opacity = document.getElementById('opacity_' + hidden.name);
        const checkbox = document.getElementById('checkbox_' + hidden.name);

        function updateHidden () {
            hidden.value = 'rgba(' + parseInt(color.value.substr(1, 2), 16).toString() + ',' +
                parseInt(color.value.substr(3, 2), 16).toString() + ',' + 
                parseInt(color.value.substr(5, 2), 16).toString() + ',' +
                opacity.value + ')';
        }

        function enableInputs() {
            color.disabled = false;
            text.disabled = false;
            number.disabled = false;
            opacity.disabled = false;
        }

        function disableInputs() {
            color.disabled = true;
            text.disabled = true;
            number.disabled = true;
            opacity.disabled = true;
        }

        if (hidden.value) {
            let vals = hidden.value.replace(/rgba\(/g, '').replace(/\)/g, '').split(',');
            color.value = '#' + Number(vals[0]).toString(16) + Number(vals[1]).toString(16) + Number(vals[2]).toString(16);
            opacity.value = vals[3];
            text.value = color.value;
            number.value = opacity.value;
            checkbox.checked = true;
        }
        else {
            // set some default values and disable inputs
            color.value = '#2b3035';
            opacity.value = 0.5;
            checkbox.checked = false;
            disableInputs();
        }

        text.addEventListener('change', () => { color.value = text.value; updateHidden(); });
        color.addEventListener('change', () => { text.value = color.value; updateHidden(); });
        number.addEventListener('change', () => { opacity.value = number.value; updateHidden(); });
        opacity.addEventListener('change', () => { number.value = opacity.value; updateHidden(); });
        opacity.addEventListener('input', () => { number.value = opacity.value; updateHidden(); });
        checkbox.addEventListener('change', () => {
            if (checkbox.checked) {
                enableInputs();
                updateHidden();
            }
            else {
                disableInputs();
                hidden.value = '';
            }
        });
        hidden.classList.add('ui-color');
    }
}
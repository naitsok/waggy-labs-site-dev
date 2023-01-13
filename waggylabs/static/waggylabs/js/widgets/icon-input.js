/**
 * Initializes icon input widgets on any admin page and monitors
 * for the DOM content changes and initalizes newly added icon
 * input widgets.
 * 
 * When icon input widget is used as a standalone widget, it needs to be
 * initialized when DOM is loaded, because telepath in this case is not
 * available. 
 */
(() => {
    function createAutocompleteWidgets() {
        $(".waggylabs-icon-input").each((idx, element) => {
            autocompleteAttach(element);            
        });
    }

    window.addEventListener("DOMContentLoaded", () => {
        // Check we are not inside a StreamField - then icon-input-adapter.js inits the autocompletes
        if (document.querySelector("[data-streamfield-stream-container]") === null) {
            createAutocompleteWidgets();
            let observer = new MutationObserver(() => {
                setTimeout(() => { 
                    createAutocompleteWidgets(); 
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
 * Function to attach the JQuery UI autocomplete widget
 * @param {object} element - text input for the widget attachment
 */
function autocompleteAttach(element) {
    if (!$(element).hasClass("ui-autocomplete-input")) {
        var icons = JSON.parse($(element).attr("iconsjson"));
        if ($(element).val()) {
            $(`<i class="w-field__icon ${icons[$(element).val()]}"></i>`).insertBefore($(element));
        }
        $(element).autocomplete({
            source: Object.keys(icons),
            select: (event, ui) => {
                $(element).val(ui.item.label);
                $(element).parent().find("i").remove();
                $(`<i class="w-field__icon ${icons[ui.item.label]}"></i>`).insertBefore($(element));
                return false;
            },
        }).data("ui-autocomplete")._renderItem = (ul, item) => {
            return $("<li></li>")
                .data("item.autocomplete", item)
                .append(`<i class="${icons[item.label]}"></i>&nbsp;${item.label}`)
                .appendTo(ul);
        };
    }
}
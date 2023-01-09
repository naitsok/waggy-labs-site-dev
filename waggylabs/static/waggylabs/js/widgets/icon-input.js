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
            document.addEventListener("DOMSubtreeModified", (e) => {
                setTimeout(() => { 
                    createAutocompleteWidgets(); 
                }, 50);
            });
        }
    });

})();


function autocompleteAttach(element) {
    if (!$(element).hasClass("ui-autocomplete-input")) {
        var icons = JSON.parse($("#" + $(element).attr("iconsjson")).text());
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
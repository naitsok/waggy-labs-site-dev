(function () {
    function createAutocompleteWidgets() {
        $(".waggylabs-icon-input").each(function (idx, element) {
            var icons = JSON.parse($("#" + $(element).attr("iconsjson")).text());
            if ($(element).val()) {
                $(`<i class="w-field__icon ${icons[$(element).val()]}"></i>`).insertBefore($(element));
            }
            $(element).autocomplete({
                source: Object.keys(icons),
                select: function (event, ui) {
                    $(element).val(ui.item.label);
                    $(element).parent().find("i").remove();
                    $(`<i class="w-field__icon ${icons[ui.item.label]}"></i>`).insertBefore($(element));
                    return false;
                },
            }).data("ui-autocomplete")._renderItem = function (ul, item) {
                return $("<li></li>")
                    .data("item.autocomplete", item)
                    .append(`<i class="${icons[item.label]}"></i>&nbsp;${item.label}`)
                    .appendTo(ul);
            };
        });
    }

    window.addEventListener("DOMContentLoaded", function () {
        createAutocompleteWidgets();
    });

})();
(function() {
    function IconInput(html, config) {
        this.html = html;
        this.baseConfig = config;
    }
    IconInput.prototype.render = function(placeholder, name, id, initialState) {
        placeholder.outerHTML = this.html.replace(/__NAME__/g, name).replace(/__ID__/g, id);

        var element = document.getElementById(id);
        element.value = initialState;
        if (initialState) {
            $(`<i class="w-field__icon ${icons[initialState]}"></i>`).appendBefore($(element));
        }

        var icons = JSON.parse(document.getElementById(element.getAttribute("iconsjson")).innerText);

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

        // define public API functions for the widget:
        // https://docs.wagtail.io/en/latest/reference/streamfield/widget_api.html
        return {
            idForLabel: null,
            getValue: function() {
                return element.value;
            },
            getState: function() {
                return element.value;
            },
            setState: function() {
                throw new Error('IconInput.setState is not implemented');
            },
            getTextLabel: function(opts) {
                if (!element.value) return '';
                var maxLength = opts && opts.maxLength,
                    result = element.value;
                if (maxLength && result.length > maxLength) {
                    return result.substring(0, maxLength - 1) + '…';
                }
                return result;
            },
            focus: function() {
                setTimeout(function() {
                    element.focus();
                }, 50);
            },
        };
    };

    window.telepath.register('waggylabs.widgets.IconInput', IconInput);
})();
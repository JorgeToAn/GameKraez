$(document).ready(function() {
    let minimum = 0;
    let maximum = 5000;
    
    $("#slider").slider({
        min: minimum,
        max: maximum,
        step: 1,
        values: [minimum, maximum],
        slide: function(event, ui) {
            for (var i = 0; i < ui.values.length; ++i) {
                $("input.sliderValue[data-index=" + i + "]").val(ui.values[i]);
            }
            $( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
        }
    });

    $("#amount").attr("value", "$" + minimum + " - $" + maximum);

    $("input.sliderValue").change(function() {
        var $this = $(this);
        $("#slider").slider("values", $this.data("index"), $this.val());
    });
});
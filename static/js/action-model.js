action_model = Backbone.Model.extend({
    initialize: function() {

    },

    do: function(action) {
        console.log("Performing: " + action);
        $.ajax({
            url: "?" + action
        });
    },
});

color_view = Backbone.View.extend({
    tagName: "a",

    template: JST["static/templates/colors.html"],

    initialize: function() {
    
    },

    render: function(color) {
        this.$el.html(this.template());
        this.$el.find(".color-item").css("background-color",color);
        return this;
    },
});

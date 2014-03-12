lights_view = Backbone.View.extend({
    el: "#main",

    events: {
        "click .do-lights-off" : "lightsOff",
        "click .do-lights-on" : "lightsOn",
        "click .do-lights-color" : "lightsColor",
        "click .do-show-colors" : "showColors",
        "click .do-door-page" : "renderDoorPage"
    },
    
    template: JST["static/templates/lights.html"],

    initialize: function() {
        this.colors = ["white", "violet", "blue", "lightblue", "aqua", "lightgreen", "green", "lime", "yellow", "orange", "red", "pink"];
    },

    render: function() {
        this.$el.html(this.template());
        
        _.each(this.colors, function(color) {
            this.addColor(color);
        }, this);
        
        return;
    },

    addColor: function(color) {
        var view = new color_view({
            className: "do-lights-color " + color
        });
        this.$(".colors").append(view.render().el);
        view.render(color);
    },

    showColors: function() {
        this.$(".colors").collapse("toggle");
    },

    lightsOn: function() {
        this.model.do("lights=on");
    },

    lightsOff: function() {
        this.model.do("lights=off");
    },

    lightsColor: function(event) {
        var color = event.currentTarget.className.split("do-lights-color ")[1];
        this.model.do("color=" + color);
    },

    renderDoorPage: function() {
        var doorPage = new door_view({
            model: this.model
        });
        this.undelegateEvents();
        doorPage.render();
    }
});

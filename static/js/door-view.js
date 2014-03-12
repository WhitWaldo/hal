door_view = Backbone.View.extend({
    el: "#main",

    events: {
        "click .do-buzz-door" : "buzzDoor",
        "click .do-lock-door" : "lockDoor",
        "click .do-unlock-door" : "unlockDoor",
        "click .do-lights-page" : "renderLightsPage"
    },

    template: JST["static/templates/door.html"],

    initialize: function() {
    },

    render: function() {
        this.$el.html(this.template());
        return;
    },

    buzzDoor: function() {
        this.model.do("door=open");
    },

    lockDoor: function() {
        this.model.do("door=lock");
    },

    unlockDoor: function() {
        this.model.do("door=unlock");
    },

    renderLightsPage: function() {
        var lightsPage = new lights_view({
            model: this.model
        });
        this.undelegateEvents();
        lightsPage.render();
    },
});

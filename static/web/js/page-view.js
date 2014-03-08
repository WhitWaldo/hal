page_view = Backbone.View.extend({
    el: "#main",

    events: {
        "click .do-buzz-door" : "buzzDoor",
        "click .do-lock-door" : "lockDoor",
        "click .do-unlock-door" : "unlockDoor",
        "click .do-lights-page" : "lightsPage"
    },
    
    initialize: function() {

    },

    render: function() {
        
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

    lightsPage: function() {
        this.model.do("lights=off");
    }
});

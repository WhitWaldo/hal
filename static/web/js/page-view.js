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
        alert("buzzDoor");
    },

    lockDoor: function() {
        alert("lockDoor");
    },

    unlockDoor: function() {
        alert("unlockDoor");
    },

    lightsPage: function() {
        alert("lightsPage");
    }
});

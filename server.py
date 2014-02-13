from flask import Flask
from door_controller import open_door
from light_controller import change_lights

app = Flask(__name__)

@app.route("/")
def default():
    return "Doorman"

@app.route("/open")
def open():
    return open_door.open()

@app.route("/lights/<command>")
def lights_change_function(command):
    return change_lights.change_function(command)

@app.route("/lights/color/<color>")
def lights_change_color(color):
    return change_lights.change_color(color)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

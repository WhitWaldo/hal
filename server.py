from flask import Flask
from flask import render_template
from flask import request
from door_controller import open_door
from light_controller import change_lights

app = Flask(__name__)

@app.route("/")
def default():
    if request.form.get("lights") is not None:
        lights_change_function(request.form.get("lights"))
    elif request.form.get("color") is not None:
        lights_change_color(request.form.get("color"))
    elif request.form.get("door") == "open":
        open()
    return render_template("index.html")

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
    app.run(host="0.0.0.0", port=80)
    # dev settings
    # app.run(host="0.0.0.0", port=8080, debug=True)

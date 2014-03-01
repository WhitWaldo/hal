from flask import Flask
from flask import render_template
from flask import request
from door_controller import open_door
from light_controller import change_lights

app = Flask(__name__)

@app.route("/")
def default():
    print(request.args)
    if request.args.get("door") == "open":
        open()
    elif request.args.get("door") == "buzz":
        buzz()
    elif request.args.get("door") == "unlock":
        unlock()
    elif request.args.get("door") == "lock":
        lock()
    elif request.args.get("lights") is not None:
        lights_change_function(request.args.get("lights"))
    elif request.args.get("color") is not None:
        lights_change_color(request.args.get("color"))

    return render_template("index.html")

@app.route("/door/open")
def open():
    return open_door.buzz() + " and " + open_door.unlock()

@app.route("/door/buzz")
def buzz():
    return open_door.buzz()

@app.route("/door/unlock")
def unlock():
    return open_door.unlock()

@app.route("/door/lock")
def lock():
    return open_door.lock()

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

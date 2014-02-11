from flask import Flask
from door_controller import open_door

app = Flask(__name__)

@app.route("/")
def default():
    return "Doorman"

@app.route("/open")
def open():
    open_door
    return "Opened"

if __name__ == "__main__":
    app.run()

from flask import Flask, render_template, redirect, request, url_for, session
from flask_oauth import OAuth
from urllib2 import Request, urlopen, URLError
from threading import Timer
import json

from door_controller import open_door
from light_controller import change_lights
import settings

app = Flask(__name__)
app.secret_key = settings.SECRET_KEY
app.debug = True

# Google OAuth setup
oauth = OAuth()
google = oauth.remote_app("google",
        base_url="https://www.google.com/accounts/",
        authorize_url = "https://accounts.google.com/o/oauth2/auth",
        request_token_url = None,
        request_token_params = {
            "scope": "https://www.googleapis.com/auth/userinfo.email",
            "response_type": "code"
        },
        access_token_url = "https://accounts.google.com/o/oauth2/token",
        access_token_method = "POST",
        access_token_params = {"grant_type": "authorization_code"},
        consumer_key = settings.GOOGLE_CLIENT_ID,
        consumer_secret = settings.GOOGLE_CLIENT_SECRET
    )
@google.tokengetter
def get_access_token():
    return session.get("access_token")

@app.route("/")
def default():
    if request.args.get("door") == "open":
        open_doors()
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
def open_doors():
    return buzz() + " and " + unlock()

@app.route("/door/buzz")
def buzz():
    return open_door.buzz()

@app.route("/door/unlock")
def unlock():
    Timer(10 * 60, lock).start()
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

@app.route("/login")
def login():
    callback = url_for("authorized", _external=True)
    return google.authorize(callback=callback)

@app.route("/authorized")
@google.authorized_handler
def authorized(resp):
    access_token = resp.get("access_token"), ""
    session["access_token"] = access_token
    # Verify user
    headers = {"Authorization": "OAuth " + access_token[0]}
    req = Request("https://www.googleapis.com/oauth2/v1/userinfo", None, headers)
    try:
        user_info = json.load(urlopen(req))
    except URLError as e:
        if e.code is not None and e.code == 401:
            session.pop('access_token', None)
            return "Error authenticating user"
    session["email"] = user_info.get("email")
    return redirect(url_for("default"))

@app.before_request
def check_auth():
    if (
            request.endpoint != "login" and
            request.endpoint != "authorized" and
            request.endpoint != "static"
        ):
        access_token = session.get("access_token")
        if access_token is None:
            return redirect(url_for("login"))
        authorized_emails = json.load(open("auth.json")).get("emails")
        if session.get("email") not in authorized_emails:
            return "Unauthorized user"

if __name__ == "__main__":
    if app.debug:
        app.config["SERVER_NAME"] = "localhost:8083"
    else:
        app.config["SERVER_NAME"] = "localhost:80"
    app.run()

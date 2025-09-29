import os
from flask import (
    Flask,
    flash,
    render_template,
    request,
    redirect,
    session as flask_session,
    url_for,
)

app = Flask("Personal Website")
app.secret_key = "my secret key"


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
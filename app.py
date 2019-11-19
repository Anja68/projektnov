import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/fakebook")
def fakebook():
    return flask.render_template("Fakebook.html")


@app.route("/friseur")
def friseur():
    return flask.render_template("friseur.html")

@app.route("/about_me")
def aboutme():
    return flask.render_template("About_me.html")


if __name__ == '__main__':
    app.run()

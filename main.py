import flask
import random
import model



from flask import url_for, render_template

app = flask.Flask(__name__)
db = model.db

db.create_all()


@app.route("/")
def index():
    user = model.User(id=1, username="Maxi", email="maxi@hallo.at")
    db.add(user)
    db.commit()

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

@app.route("/base")
def base():
    return flask.render_template("base.html")

@app.route("/secret-number-game")
def secret_number_game():
    secret = random.randint(1, 10)
    attemps = 0
    return flask.render_template("secret_number_game.html", secret_number=secret)

@app.route("/blog")
def blog():
    receipe_1 = model.Receipe ("Apfelstrudel", "Cut Apple Bake Sweet", "Sweet")
    receipe_2 = model.Receipe ("Hamburger", "Fry Meat And Eat", "Sour")
    receipe_3 = model.Receipe ("Suppe", "Cut Carrots Add Water", "Salty")
    return flask.render_template("blog.html", receipes=[receipe_1, receipe_2, receipe_3])


if __name__ == '__main__':
    app.run()

import flask
import random
import model
import string


from flask import request
from flask import url_for, render_template

N_USERS = 10
N_RECEPIES = 10
N_BOOKS = 10

app = flask.Flask(__name__)
db = model.db

db.create_all()

def create_dummy_users():
    users = []
    for x in range(N_USERS):
        name = "".join(random.choices(string.ascii_lowercase, k=10))
        user = model.User(username=name, email=f"{name}@home.com")
        users.append(user)

    my_user = model.User(username="admin", email="admin@home.com")
    users.append(my_user)
    test_user = model.User(username="test", email="test@home.com")
    users.append(test_user)

    for user in users:
        if not db.query(model.User).filter_by(username=user.username).first():
            db.add(user)

    db.commit()

def create_dummy_recepies():
    recepies = []
    for x in range(N_RECEPIES):
        name = "".join(random.choices(string.ascii_lowercase, k=10))
        name = name.capitalize()
        description = "".join(random.choices(string.ascii_lowercase + "    ", k=80))
        taste = "".join(random.choices(string.ascii_lowercase + "    ", k=20))
        new_receipe = model.Receipe(name=name, description=description, taste=taste)
        recepies.append(new_receipe)

    receipe_1 = model.Receipe(name="Apfelstrudel", description="Cut Apple Bake Sweet", taste="sweet")
    recepies.append(receipe_1)
    receipe_2 = model.Receipe(name="Hamburger", description="Fry Meat And Eat", taste="sour")
    recepies.append(receipe_2)
    receipe_3 = model.Receipe(name="Suppe", description="Fry Meat And Drink", taste="bitter")
    recepies.append(receipe_3)

    for receipe in recepies:
        if not db.query(model.Receipe).filter_by(name=receipe.name).first():
            db.add(receipe)

    db.commit()



def create_dummy_books():
    bookslist = []
    for x in range(N_BOOKS):
        title = "".join(random.choices(string.ascii_lowercase, k=10))
        bookdescription = "".join(random.choices(string.ascii_lowercase + "    ", k=20))
        new_book = model.books(title=title, bookdescription=bookdescription)
        bookslist.append(new_book)

        book_1 = model.books(title="True Story", bookdescription="About the world we live in")
        bookslist.append(book_1)
        book_2 = model.books(title="Another Story", bookdescription="About the next generation")
        bookslist.append(book_2)
        book_3 = model.books(title="ABC Book", bookdescription="Learn to dive")
        bookslist.append(book_3)

        for book in bookslist:
            if not db.query(model.books).filter_by(title=book.title).first():
                db.add(book)
    db.commit()

def add_dummy_data():
    create_dummy_users()
    create_dummy_recepies()
    create_dummy_books()


@app.route("/")
def index():

    return flask.render_template("index.html", myname="Anja")


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
    all_recepies = db.query(model.Receipe).all()
    return flask.render_template('blog.html', recepies=all_recepies)


@app.route("/books")
def books():
    all_books = db.query(model.books).all()
    return flask.render_template('books.html', books=all_books)

@app.route("/register", methods=["GET", "POST"])
def register():

    current_request = flask.request

    if current_request.method == "GET":
        return flask.render_template("register.html")

    elif current_request.method == "POST":
        # TODO: register valid user
        email = current_request.form.get('email')
        username = current_request.form.get('username')
        user_exists = db.query(model.User).filter_by(username=username).first()
        email_exists = db.query(model.User).filter_by(email=email).first()
        if user_exists:
            print("User already exists")
        elif email_exists:
            print("Email already exists")
        else:
            new_user = model.User(username=username, email=email)
            db.add(new_user)
            db.commit()
        return flask.redirect(flask.url_for('register'))

@app.route("/accounts")
def accounts():
    all_users = db.query(model.User).all()
    return flask.render_template('accounts.html', accounts=all_users)

@app.route("/accounts/<account_id>/delete", methods=["GET", "POST"])
def account_delete(account_id):
    user_to_delete = db.query(model.User).get(account_id)
    if user_to_delete is None:
        return flask.redirect(flask.url_for('accounts'))

    current_request = flask.request
    if current_request.method == "GET":
        return flask.render_template("account_delete.html", account=user_to_delete)
    elif current_request.method == "POST":
        db.delete(user_to_delete)
        db.commit()
        return flask.redirect(flask.url_for('accounts'))

@app.route("/books/<book_id>/delete", methods=["GET", "POST"])
def book_delete(book_id):
    book_to_delete = db.query(model.books).get(book_id)
    if book_to_delete is None:
        return flask.redirect(flask.url_for('books'))

    current_request = flask.request
    if current_request.method == "GET":
        return flask.render_template("books_delete.html", book=book_to_delete)
    elif current_request.method == "POST":
        db.delete(book_to_delete)
        db.commit()
        return flask.redirect(flask.url_for('books'))


if __name__ == '__main__':
    add_dummy_data()
    app.run()

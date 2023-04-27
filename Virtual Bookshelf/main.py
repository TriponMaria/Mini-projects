from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///all-books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


# Create a new table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


@app.route('/add', methods=["POST", "GET"])
def add():
    if request.method == "POST":
        book = Book(
            title=request.form["book_name"],
            author=request.form["author_name"],
            rating=request.form["rating"])
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit', methods=["POST", "GET"])
def edit_rating():
    all_books = db.session.query(Book).all()
    if request.method == "POST":
        book_id = request.form['book_id']
        rating_update = Book.query.filter_by(id=book_id).first()
        rating_update.rating = request.form["new_rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = int(request.args.get('id'))
    return render_template('edit.html', books=all_books, book_id=book_id)


@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    book_to_delete = db.session.get(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)

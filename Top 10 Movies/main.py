from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import ast
import requests
import os

API_KEY = os.environ['API_KEY']
MOVIES_DB_URL = os.environ['MOVIES_DB_URL']

db = SQLAlchemy()
app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
Bootstrap(app)


# Create table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()


class RateMovieForm(FlaskForm):
    rating = StringField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review: ', validators=[DataRequired()])
    done = SubmitField('Done')


class MovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    add_movie = SubmitField('Add Movie')


@app.route('/')
def home():
    all_movies = db.session.query(Movie).order_by(Movie.rating.desc()).all()
    print("all_movies ", all_movies)
    for movie in all_movies:
        movie.ranking = all_movies.index(movie) + 1
        print(movie.title)
    return render_template("index.html", all_movies=all_movies)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    all_movies = db.session.query(Movie).all()
    movie_id = int(request.args.get('id'))
    form = RateMovieForm()
    if form.validate_on_submit():
        new_rating = form.rating.data
        new_review = form.review.data
        update = Movie.query.filter_by(id=movie_id).first()
        update.rating = new_rating
        update.review = new_review
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', all_movies=all_movies, movie_id=movie_id, form=form)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.session.get(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['POST', 'GET'])
def add_movie():
    form = MovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        movie_title = str(movie_title).replace(" ", "")
        parameters = {
            "api_key": API_KEY,
            "query": movie_title
        }
        response = requests.get(MOVIES_DB_URL, params=parameters)
        results = response.json()['results']
        return render_template('select.html', results=results)
    return render_template('add.html', form=form)


@app.route('/select')
def select():
    results = request.args.get('id')
    results_dict = ast.literal_eval(results)
    print(results_dict)
    print(type(results_dict))

    new_movie = Movie(
        title=results_dict["original_title"],
        year=results_dict["release_date"],
        description=results_dict["overview"],
        rating=round(float(results_dict["vote_average"]), 1),
        ranking=1,
        review="None",
        img_url="https://image.tmdb.org/t/p/w500/" + results_dict["poster_path"]
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

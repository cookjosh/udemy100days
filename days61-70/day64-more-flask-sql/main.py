from flask import Flask, render_template, redirect, url_for, request, session
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from forms import UpdateForm, AddMovie
import json
import os
import requests
import urllib.parse


db = SQLAlchemy()
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top-movies.db'
db.init_app(app)

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, unique=True, nullable=True)
    year = db.Column(db.Integer, unique=False, nullable=True)
    description = db.Column(db.String, unique=False, nullable=True)
    rating = db.Column(db.Float, unique=False, nullable=True)
    ranking = db.Column(db.Integer, unique=True, nullable=True)
    review = db.Column(db.String, nullable=True)
    img_url = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f'<Movie {self.title}>'

with app.app_context():
    db.create_all()

movie_api_string = f'?api_key={os.environ.get("MOVIE_DB_TOKEN")}'
movie_search_url = f"https://api.themoviedb.org/3/search/movie/{movie_api_string}&"
movie_detail_url = "https://api.themoviedb.org/3/movie/"
movie_poster_url = "https://image.tmdb.org/t/p/original"

@app.route("/")
def home():
    movies=Movies.query.order_by(Movies.rating).all()
    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
    db.session.commit()
    return render_template("index.html", movies=movies)

@app.route("/edit", methods=['GET', 'POST'])
def edit(movie=None):
    form = UpdateForm()
    movie = Movies.query.filter_by(id=(request.args.get('id'))).first()
    if form.validate_on_submit():
        if movie == None:
            movie = Movies.query.order_by(Movies.id.desc()).first()
            rating = form.rating.data
            review = form.review.data
            movie.rating = rating
            movie.review = review
            db.session.commit()  
            return redirect(url_for('home'))
        else:
            rating = form.rating.data
            review = form.review.data
            movie.rating = rating
            movie.review = review
            db.session.commit()  
            return redirect(url_for('home'))
    return render_template("edit.html", form=form)

@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    db.session.delete(Movies.query.get(movie_id))
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        title = form.title.data
        movie_query = urllib.parse.urlencode({'query': title})
        response = requests.get(url=f'{movie_search_url}{movie_query}')
        results = response.json()['results']
        return render_template("select.html", results=results)
    return render_template("add.html", form=form)

@app.route("/select")
def select():
    movie_id = request.args.get('id')
    response = requests.get(url=f'{movie_detail_url}{movie_id}{movie_api_string}')
    poster_path = response.json()['poster_path']
    new_movie = Movies(title=response.json()['original_title'], description=response.json()['overview'], year=response.json()['release_date'], img_url=f'{movie_poster_url}{poster_path}', rating=0, review="")
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit'))

if __name__ == '__main__':
    app.run(debug=True)
    
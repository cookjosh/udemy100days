from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'

db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'
        
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('index.html', books=db.session.query(Book).all())


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book_name = request.form.get('book_name')
        book_author = request.form.get('book_author')
        book_rating = request.form.get('book_rating')
        db.session.add(Book(title = book_name, author = book_author, rating = book_rating))
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/edit')
def edit():
    return render_template('edit.html')


if __name__ == '__main__':
    app.run(debug=True)
    


from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms import LoginForm

def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    


    app.secret_key = {{SECRET_KEY}}


    @app.route("/")
    def home():
        return render_template('index.html')

    @app.route("/login", methods=["GET", "POST"])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            if form.email.data == "admin@email.com" and form.password.data == "12345678":
                return render_template('success.html')
            else:
                return render_template('denied.html')
        return render_template('login.html', form=form)

    return app

if __name__ == '__main__':
    create_app()
    app.run(debug=True)
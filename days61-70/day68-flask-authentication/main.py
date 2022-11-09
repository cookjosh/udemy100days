from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("name")
        email = request.form.get("email")
        password_hash = generate_password_hash(request.form.get("password"), "pbkdf2:sha256")
        active_user = db.session.query(User).filter(User.email == email).first()
        if active_user:
            flash("Email already in use!")
            return redirect(url_for("register"))
        else:
            new_user = User(email = email, password = password_hash, name = username)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("secrets", logged_in = True))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    error = None
    all_users = db.session.query(User).all()
    all_usernames = []
    for user in all_users:
        all_usernames.append(user.email)
    print(all_usernames)
    if request.method == "POST":
        email = request.form.get("email")
        if email not in all_usernames:
            flash("Username not found")
            return redirect(url_for("login"))
        else:
            active_user = db.session.query(User).filter(User.email == email).first()
            if check_password_hash(active_user.password, request.form.get("password")):
                login_user(active_user)
                flash("Successful login!")
                return redirect(url_for("secrets", logged_in = True))
            else:
                flash("Incorrect Username or Password")
                return redirect(url_for("login"))
    return render_template("login.html", error=error)


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", username = current_user.name)


@app.route('/logout')
def logout():
    pass


@app.route('/download')
@login_required
def download():
    return send_from_directory(f"{app.root_path}/static/files", "cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)

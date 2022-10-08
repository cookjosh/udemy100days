from symbol import power
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()] )
    open_time = StringField('Open Time (e.g. 8AM)', validators=[DataRequired()])
    close_time = StringField('Closing Time (e.g. 6PM)', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating ☕️', choices=[(1, "☕️"), ("☕️☕️", "☕️☕️"), ("☕️☕️☕️", "☕️☕️☕️"), ("☕️☕️☕️☕️", "☕️☕️☕️☕️"), ("☕️☕️☕️☕️☕️", "☕️☕️☕️☕️☕️")] ,validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Rating 💪', choices=[("💪", "💪"), ("💪💪", "💪💪"), ("💪💪💪", "💪💪💪"), ("💪💪💪💪", "💪💪💪💪"), ("💪💪💪💪💪", "💪💪💪💪💪")], validators=[DataRequired()])
    power_rating = SelectField('Power Availability Rating 🔌', choices=[("🔌", "🔌"), ("🔌🔌", "🔌🔌"), ("🔌🔌🔌", "🔌🔌🔌"), ("🔌🔌🔌🔌", "🔌🔌🔌🔌"), ("🔌🔌🔌🔌🔌", "🔌🔌🔌🔌🔌")], validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_name = form.cafe.data
        cafe_location = form.cafe_location.data
        open_time = form.open_time.data
        close_time = form.close_time.data
        coffee_rating = form.coffee_rating.data
        wifi_rating = form.wifi_rating.data
        power_rating = form.power_rating.data
        with open('cafe-data.csv', 'a') as csv_file:
            csv_file.write(f'{cafe_name},{cafe_location},{open_time},{close_time},{coffee_rating},{wifi_rating},{power_rating} \n')
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

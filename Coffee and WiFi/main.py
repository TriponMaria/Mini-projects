from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
import os

rating_choices = [i * '☕' for i in range(1, 6)]
wifi_choices = ['✘'] + [i * '💪' for i in range(1, 6)]
power_choices = ['✘'] + [i * '🔌' for i in range(1, 6)]

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe_name = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps(URL)', validators=[DataRequired(), URL()])
    open = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    rating = SelectField('Coffee Rating', choices=rating_choices, validators=[DataRequired()])
    wifi = SelectField('Wifi Strength Rating', choices=wifi_choices, validators=[DataRequired()])
    power = SelectField('Power Socket Availability', choices=power_choices, validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    row = [form.cafe_name.data,
           form.location.data,
           form.open.data,
           form.close.data,
           form.rating.data,
           form.wifi.data,
           form.power.data]
    if form.validate_on_submit():
        print("True")
        with open('cafe-data.csv', 'at', encoding='utf8') as csv_file:
            csv_file.write('\n')
            for item in row:
                csv_file.write(item + ',')
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open("cafe-data.csv", newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        print(csv_data)
        list_of_rows = []
        for row in csv_data:
            print(row)
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email





app = Flask(__name__)

bootstrap = Bootstrap5(app)

class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(message="Fill in sth"), Email(check_deliverability=True, message="Invalid email")])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8, message="Password must be more than eight characters")])
    submit_button = SubmitField(label="Login")


app.secret_key = 'secret_key'
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        print(request.url_rule.methods)
        if form.email.data == 'manuels@gmail.com' and form.password.data == '12345678':
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)

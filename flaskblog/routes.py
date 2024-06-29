from flask import render_template, url_for, flash, redirect
from run import app
from flaskblog.forms import Registrationform, Loginform
from flaskblog.models import User, Post


posts =[
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First Blog Post',
        'date': 'June 22, 2024'
    },
    {
        'author': 'Ogbonnaya Kelechi',
        'title': 'Blog Post 2',
        'content': 'Second Blog Post',
        'date': 'June 22, 2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = Registrationform()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = Loginform()
    return render_template('login.html', title='Login', form=form)



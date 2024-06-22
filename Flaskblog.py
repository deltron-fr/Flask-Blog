from flask import Flask, render_template, url_for
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
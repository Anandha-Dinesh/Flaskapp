from flask import Flask,render_template,request
import random

app = Flask(__name__)

relationship_quotes = [
    {"quote": "A successful marriage requires falling in love many times, always with the same person.", "author": "Mignon McLaughlin"},
    {"quote": "The best thing to hold onto in life is each other.", "author": "Audrey Hepburn"},
    {"quote": "We are most alive when we’re in love.", "author": "John Updike"},
    {"quote": "Love is not about how many days, months, or years you have been together. Love is about how much you love each other every single day.", "author": "Unknown"},
    {"quote": "True love stories never have endings.", "author": "Richard Bach"},
    {"quote": "To love and be loved is to feel the sun from both sides.", "author": "David Viscott"},
    {"quote": "Love doesn’t make the world go ‘round. Love is what makes the ride worthwhile.", "author": "Franklin P. Jones"},
    {"quote": "The greatest thing you’ll ever learn is just to love and be loved in return.", "author": "Eden Ahbez"},
    {"quote": "A great relationship doesn’t happen because of the love you had in the beginning, but how well you continue building love until the end.", "author": "Unknown"},
    {"quote": "The best love is the kind that awakens the soul and makes us reach for more.", "author": "Nicholas Sparks"}
]


@app.route('/', methods=['GET', 'POST'])
def home():
    Q = random.choice(relationship_quotes)
    return render_template('index.html',quote=Q['quote'],author=Q['author'])

@app.route('/about',methods=['GET', 'POST'])
def about():
    return "this is the about page"


app.run(debug=True)

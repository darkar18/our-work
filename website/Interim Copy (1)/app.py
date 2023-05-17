from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/edit')
def edit():
    return render_template('index3.html')

@app.route('/txt')
def text():
    return render_template('index2.html')

@app.route('/drp')
def dropdown():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
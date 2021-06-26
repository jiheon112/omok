from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    return 'search'

@app.route('/no')
def no():
    return 'no'

if __name__ == '__main__':
    app.run(debug=True)
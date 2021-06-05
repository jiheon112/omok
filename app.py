from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'omok'

@app.route('/search')
def search():
    return 'search'

if __name__ == '__main__':
    app.run(debug=True)
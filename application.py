from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def home():
    return render_template('index.html')

@application.route('/search')
def search():
    return 'search'

@application.route('/no')
def no():
    return 'no'

if __name__ == '__main__':
    application.run(debug=False)
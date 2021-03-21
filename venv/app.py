from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')

def home():
    return 'Hello jinsol1'

@app.route('/user')

def user():
    return 'Hello user2'

if(__name__ == '__main__'):
    app.run(debug=True)

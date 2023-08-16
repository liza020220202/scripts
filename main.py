from flask import Flask


app = Flask('my first app')


@app.route('/')
@app.route('/index')
def hi_flask():
    return 'https://github.com/liza020220202'


@app.route('/login')
def login():
    return 'You are on login'


app.run(debug=True)

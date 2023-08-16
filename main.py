from flask import Flask, render_template


app = Flask('my first app')


@app.route('/')
@app.route('/index')
def hi_flask():
    return render_template('index.html')


@app.route('/login')
def login():
    return 'Login'


app.run(debug=True)
@app.route(f"/user/<username>")
def hello(username):
    return render_template('hello.html', username=username)

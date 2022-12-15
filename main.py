from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/login/')
def about():
    return render_template('login.html')

@app.route('/signup/')
def contact():
    return render_template('signup.html')

if  __name__=='__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
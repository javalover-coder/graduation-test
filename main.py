from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/logout")
def logout():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='localhost', port=5555)
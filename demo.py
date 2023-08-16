from flask import *;

app = Flask(__name__);

@app.route('/')
def home():
    return "<h1>My Python App 1.0</h1>"

if __name__ == "__main__":
    app.run()




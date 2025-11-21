from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Demo is demoing"

if __name__ == "__main__":
    app.run()

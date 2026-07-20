from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to SOCSight"

@app.route("/about")
def about():
    return "SOCSight is a Mini SIEM built with Flask."

@app.route("/health")
def health():
    return "Application Status: Healthy"

if __name__ == "__main__":
    app.run(debug=True)
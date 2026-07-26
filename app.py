from flask import Flask, render_template, request
import os
from parser.linux_parser import parse_logs
app = Flask(__name__)

# Folder to store uploaded log files
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["logfile"]

    if file.filename == "":
        return "No file selected."

    # Save uploaded file
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Read the log file line by line
    logs = []

    parsed_logs = parse_logs(filepath)
    output = ""

    for log in parsed_logs:
     output += f"""
    Timestamp : {log['timestamp']}
    Level     : {log['level']}
    Event     : {log['event']}
    User      : {log['user']}
    IP        : {log['ip']}

    -------------------------

    """

    return "<pre>" + output + "</pre"




if __name__ == "__main__":
    app.run(debug=True)
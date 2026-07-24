from flask import Flask, render_template, request
import os

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

    parsed_logs = []

    with open(filepath, "r") as file:
     for line in file:

        line = line.strip()
        if not line:
            continue
        parts = line.split()

        timestamp = parts[0] + " " + parts[1]
        level = parts[2]
        event = parts[3]
        user = parts[4].split("=")[1]
        ip = parts[5].split("=")[1]

        parsed_logs.append(
            f"""
    Timestamp : {timestamp}
    Level     : {level}
    Event     : {event}
    User      : {user}
    IP        : {ip}

    -------------------------
    """
        )

    return "<pre>" + "".join(parsed_logs) + "</pre>"


if __name__ == "__main__":
    app.run(debug=True)
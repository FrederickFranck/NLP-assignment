import os
from tokenize import String
from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
import pathlib

ALLOWED_EXTENSIONS = set(["txt"])
UPLOAD_FOLDER = pathlib.Path(__file__).parent / "static/uploads/"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Check to see if file is allowed
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# Replace with actual function
def predict_tax(text: String) -> bool:
    return True


@app.route("/", methods=["GET", "POST"])
def route_api():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":

        try:
            text = request.form["text"]
            print(text)
            result = predict_tax(text)
            return render_template("index.html", result=result)
        except:
            print("No text input")

        if "file" not in request.files:
            flash("No file uploaded")
            return render_template("index.html")

        file = request.files["file"]
        if file.filename == "":
            flash("No selected file")
            return render_template("index.html")

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config["UPLOAD_FOLDER"] / filename)
            print(f"path = {path}")
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            _file = open(os.path.join(app.config["UPLOAD_FOLDER"], filename), "r")
            content = _file.read()
            print(f"Content : {content}")

            # Replace with actual function
            result = predict_tax(content)
            return render_template("index.html", result=result)
        else:
            return "Something Went wrong"

if __name__ == "__main__":
    app.secret_key = "super_secret_key"
    app.config["SESSION_TYPE"] = "filesystem"
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, threaded=True, debug=True)

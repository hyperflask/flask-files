from flask import Flask, request, render_template
from flask_files import Files, save_file, validate_file
from flask_files.images import IMAGE_EXTS, create_thumbnail


app = Flask(__name__)
Files(app)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        validate_file(request.files["file"], IMAGE_EXTS)
        file = save_file(request.files["file"])
        thumb = save_file(create_thumbnail(file, 100, 100))
        return render_template("image.html", file=file, thumb=thumb)
    return render_template("upload.html")
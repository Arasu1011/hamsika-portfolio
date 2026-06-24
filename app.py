from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():

    photos = []
    certificates = []
    videos = []

    # Photos
    if os.path.exists("static/photos"):
        for file in os.listdir("static/photos"):
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                photos.append(file)

    # Certificates
    if os.path.exists("static/certificates"):
        for file in os.listdir("static/certificates"):
            if file.lower().endswith((".jpg", ".jpeg", ".png", ".pdf")):
                certificates.append(file)

    # Videos
    if os.path.exists("static/videos"):
        for file in os.listdir("static/videos"):
            if file.lower().endswith(".mp4"):
                videos.append(file)

    photos.sort()
    certificates.sort()
    videos.sort()

    return render_template(
        "index.html",
        photos=photos,
        certificates=certificates,
        videos=videos
    )

if __name__ == "__main__":
    app.run(debug=True)
from pathlib import Path

from flask import Flask, send_from_directory


BASE_DIR = Path(__file__).resolve().parent
IMAGES_DIR = BASE_DIR / "images"

app = Flask(__name__)


@app.get("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")


@app.get("/images/<path:filename>")
def images(filename: str):
    return send_from_directory(IMAGES_DIR, filename)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
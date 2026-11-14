
from flask import Flask, request, jsonify, send_file
from pathlib import Path
import cv2
import numpy as np
import base64

# Import our vesicle detection function
from detector import count_vesicles

# Create the Flask website application
app = Flask(__name__)

# Find the folder containing this file
folder = Path(__file__).resolve().parent

# Maximum uploaded image size: 15 MB
app.config["MAX_CONTENT_LENGTH"] = 15 * 1024 * 1024


# The main website page
@app.route("/")
def home():
    return send_file(folder / "index.html")


# Analyze an uploaded microscopy image
@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        # Receive image and selected grid-hole coordinates
        uploaded_file = request.files["image"]

        center_x = int(request.form["center_x"])
        center_y = int(request.form["center_y"])
        radius = int(request.form["radius"])

        # Convert uploaded image into OpenCV format
        image_bytes = np.frombuffer(
            uploaded_file.read(),
            dtype=np.uint8
        )

        image = cv2.imdecode(
            image_bytes,
            cv2.IMREAD_COLOR
        )

        if image is None:
            return jsonify(error="Invalid image"), 400

        height, width = image.shape[:2]

        # Check that the selected circle is valid
        if not (
            0 <= center_x < width
            and 0 <= center_y < height
            and 0 < radius <= max(width, height)
        ):
            return jsonify(error="Invalid selection"), 400

        # Call the function from detector.py
        count, result_image = count_vesicles(
            image,
            center_x,
            center_y,
            radius
        )

        # Convert the result image into PNG
        success, encoded_image = cv2.imencode(
            ".png",
            result_image
        )

        if not success:
            return jsonify(error="Image encoding failed"), 500

        # Convert image to text that can be sent to HTML
        image_base64 = base64.b64encode(
            encoded_image.tobytes()
        ).decode("utf-8")

        # Return the result to the website
        return jsonify({
            "count": count,
            "image": "data:image/png;base64," + image_base64
        })

    except (KeyError, ValueError, TypeError):
        return jsonify(error="Invalid request data"), 400


# Start the local website
if __name__ == "__main__":
    app.run(debug=True)

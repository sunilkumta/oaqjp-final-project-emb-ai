"""Flask server for emotion detection application."""
from flask import Flask, render_template, request
from EmotionDetection import EmotionDetection

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    """Render the main index page."""
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector():
    """Analyze text and return emotion detection results."""
    # get text from request
    text = request.args.get("textToAnalyze")
    # call emotion detector
    detector = EmotionDetection()
    #return response
    result = detector.emotion_detector(text)
    if result['dominant_emotion'] is None :
        return 'Invalid text! Please try again!.'
    return detector.emotions_info()

if __name__ == "__main__":
    app.run(host="", port=5000, debug=True)

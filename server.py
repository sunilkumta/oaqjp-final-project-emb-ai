from flask import Flask, render_template, request
from EmotionDetection import EmotionDetection
from EmotionDetection.emotion_response import EmotionResponse

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotionDetector():
    text = request.args.get("textToAnalyze")
    detector = EmotionDetection()
    result = detector.emotion_detector(text)
    emr = EmotionResponse(result)
    info = emr.emotions_info()
    return info
from flask import Flask, render_template, request
from EmotionDetection import EmotionDetection
from EmotionDetection.emotion_response import EmotionResponse

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotionDetector():
    # get text from request
    text = request.args.get("textToAnalyze")
    # call emotion detector
    detector = EmotionDetection()
    result = detector.emotion_detector(text)
    # interpret result
    emr = EmotionResponse(result)
    emotions_json = emr.emotions()
    # check for invalid text and return appropriate response
    if (emotions_json['dominant_emotion'] is None):
        return "Invalid text! Please try again!."
    else:
        ret = emr.emotions_info()
        print(ret)
        return ret

if __name__ == "__main__":
    app.run(host="", port=5000, debug=True)
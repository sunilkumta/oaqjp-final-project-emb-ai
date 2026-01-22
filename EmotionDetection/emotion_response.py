import json

class EmotionResponse:
    """class to interpret result"""

    def __init__(self, result_text):
        """constr"""
        self.result_json = json.loads(result_text)

        # Check for error in the response and set emotions to None
        if ("emotionPredictions" not in self.result_json and "code" in self.result_json) :
            self.emotions_json = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
            return

        # Create necessary info
        self.emotions_json = self.result_json["emotionPredictions"][0]["emotion"]
        dominant = max(self.emotions_json, key=self.emotions_json.get)
        self.emotions_json['dominant_emotion'] = dominant

    def emotions(self):
        """return emotion"""
        return self.emotions_json

    def emotions_info(self):
        """string representation"""
        return f"For the given statement, the system response is 'anger': {self.emotions()['anger']}, 'disgust': {self.emotions()['disgust']}, 'fear': {self.emotions()['fear']}, 'joy': {self.emotions()['joy']} and 'sadness': {self.emotions()['sadness']}. The dominant emotion is {self.emotions()['dominant_emotion']}."



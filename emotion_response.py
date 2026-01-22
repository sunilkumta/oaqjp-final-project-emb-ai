import json

class EmotionResponse:
    """class to interpret result"""

    def __init__(self, result_text):
        """constr"""
        self.result_json = json.loads(result_text)

        # Check for error in the response
        if ("emotionPredictions" not in self.result_json and "code" in self.result_json) :
            raise Exception(self.result_json["message"])

        # Create necessary info
        self.emotions_json = self.result_json["emotionPredictions"][0]["emotion"]
        dominant = max(self.emotions_json, key=self.emotions_json.get)
        self.emotions_json['dominant_emotion'] = dominant

    def emotions(self):
        """return emotion"""
        return self.emotions_json

    def emotions_info(self):
        """string representation"""
        return f"For the given statement, the system response is 'anger': {self.emotions()['anger']}, 'disgust': {self.emotions()['anger']}, 'fear': {self.emotions()['anger']}, 'joy': {self.emotions()['anger']} and 'sadness': {self.emotions()['anger']}. The dominant emotion is {self.emotions()['anger']}."



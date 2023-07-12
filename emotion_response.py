import json

class EmotionResponse:
    """class to interpret result"""

    def __init__(self, result_text):
        """constr"""
        self.result_json = json.loads(result_text)

    def emotion(self):
        """return emotion"""
        return "self.result_json"


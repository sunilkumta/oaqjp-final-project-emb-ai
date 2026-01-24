import requests
import json

class EmotionDetection:
    """Class representing emotion detection."""
    URL =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    def __init__(self):
        """constructor."""

    def emotion_detector(self, text_to_analyze):
        """method to detect emotion."""
        input_dict = { "raw_document": { "text": text_to_analyze }}

        #make request
        self.response = requests.post(self.URL, json = input_dict, headers=self.HEADERS)

        # handle error condition
        if (self.response.status_code == 400):
            self.emotions_json = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
            return

        #convert request into usable form
        self.convert_response_to_json()

        print(json.dumps(self.emotions_json, indent=4))

    def convert_response_to_json(self):
        """Interpret results."""
        #convert result text to json
        self.result_json = json.loads(self.response.text)

        #get emotions json
        self.emotions_json = self.result_json["emotionPredictions"][0]["emotion"]

        # get key of max emotion score
        dominant = max(self.emotions_json, key=self.emotions_json.get)
        self.emotions_json['dominant_emotion'] = dominant

    def emotions_info(self):
        """string representation"""
        return f"For the given statement, the system response is 'anger': {self.emotions_json['anger']}, 'disgust': {self.emotions_json['disgust']}, 'fear': {self.emotions_json['fear']}, 'joy': {self.emotions_json['joy']} and 'sadness': {self.emotions_json['sadness']}. The dominant emotion is {self.emotions_json['dominant_emotion']}."
        

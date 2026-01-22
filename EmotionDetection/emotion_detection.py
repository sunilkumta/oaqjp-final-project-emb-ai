"""Module representing emotion detection."""
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
        response = requests.post(self.URL, json = input_dict, headers=self.HEADERS)
        return response.text

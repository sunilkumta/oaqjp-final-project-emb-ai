"""Module representing emotion detection."""
import requests
import json

class EmotionDetection:
    """Class representing emotion detection."""
    URL =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # TODO I used these sample responses by running prompts once, to minimize cost of calling model while developing and 
    # testing application. 
    # responses = json.loads("""
    #     {
    #         "": {
    #                 "code": 3,
    #                 "details": [],
    #                 "message": "Exception raised during inference. This may be a problem with your input: value check failed: Input RawDocument object `raw_document` cannot be empty"
    #         },        
    #         "I am glad this happened": {
    #             "emotionPredictions": [
    #                 {
    #                     "emotion": {
    #                         "anger": 0.01388365,
    #                         "disgust": 0.00850114,
    #                         "fear": 0.018487887,
    #                         "joy": 0.83237535,
    #                         "sadness": 0.17257097
    #                     },
    #                     "emotionMentions": [
    #                         {
    #                             "emotion": {
    #                                 "anger": 0.01388365,
    #                                 "disgust": 0.00850114,
    #                                 "fear": 0.018487887,
    #                                 "joy": 0.83237535,
    #                                 "sadness": 0.17257097
    #                             },
    #                             "span": {
    #                                 "begin": 0,
    #                                 "end": 23,
    #                                 "text": "I am glad this happened"
    #                             }
    #                         }
    #                     ],
    #                     "target": ""
    #                 }
    #             ],
    #             "producerId": {
    #                 "name": "Ensemble Aggregated Emotion Workflow",
    #                 "version": "0.0.1"
    #             }
    #         },
    #         "I am really afraid that this will happen": {
    #             "emotionPredictions": [
    #                 {
    #                     "emotion": {
    #                         "anger": 0.0068210675,
    #                         "disgust": 0.00360616,
    #                         "fear": 0.9907291,
    #                         "joy": 0.0057615982,
    #                         "sadness": 0.073330835
    #                     },
    #                     "emotionMentions": [
    #                         {
    #                             "emotion": {
    #                                 "anger": 0.0068210675,
    #                                 "disgust": 0.00360616,
    #                                 "fear": 0.9907291,
    #                                 "joy": 0.0057615982,
    #                                 "sadness": 0.073330835
    #                             },
    #                             "span": {
    #                                 "begin": 0,
    #                                 "end": 40,
    #                                 "text": "I am really afraid that this will happen"
    #                             }
    #                         }
    #                     ],
    #                     "target": ""
    #                 }
    #             ],
    #             "producerId": {
    #                 "name": "Ensemble Aggregated Emotion Workflow",
    #                 "version": "0.0.1"
    #             }
    #         },
    #         "I am really mad about this": {
    #             "emotionPredictions": [
    #                 {
    #                     "emotion": {
    #                         "anger": 0.6674731,
    #                         "disgust": 0.022848725,
    #                         "fear": 0.09749009,
    #                         "joy": 0.011863918,
    #                         "sadness": 0.1953058
    #                     },
    #                     "emotionMentions": [
    #                         {
    #                             "emotion": {
    #                                 "anger": 0.6674731,
    #                                 "disgust": 0.022848725,
    #                                 "fear": 0.09749009,
    #                                 "joy": 0.011863918,
    #                                 "sadness": 0.1953058
    #                             },
    #                             "span": {
    #                                 "begin": 0,
    #                                 "end": 26,
    #                                 "text": "I am really mad about this"
    #                             }
    #                         }
    #                     ],
    #                     "target": ""
    #                 }
    #             ],
    #             "producerId": {
    #                 "name": "Ensemble Aggregated Emotion Workflow",
    #                 "version": "0.0.1"
    #             }
    #         },
    #         "I am so sad about this": {
    #             "emotionPredictions": [
    #                 {
    #                     "emotion": {
    #                         "anger": 0.0063314,
    #                         "disgust": 0.005223638,
    #                         "fear": 0.074054584,
    #                         "joy": 0.0046975184,
    #                         "sadness": 0.9819713
    #                     },
    #                     "emotionMentions": [
    #                         {
    #                             "emotion": {
    #                                 "anger": 0.0063314,
    #                                 "disgust": 0.005223638,
    #                                 "fear": 0.074054584,
    #                                 "joy": 0.0046975184,
    #                                 "sadness": 0.9819713
    #                             },
    #                             "span": {
    #                                 "begin": 0,
    #                                 "end": 22,
    #                                 "text": "I am so sad about this"
    #                             }
    #                         }
    #                     ],
    #                     "target": ""
    #                 }
    #             ],
    #             "producerId": {
    #                 "name": "Ensemble Aggregated Emotion Workflow",
    #                 "version": "0.0.1"
    #             }
    #         },
    #         "I feel disgusted just hearing about this": {
    #             "emotionPredictions": [
    #                 {
    #                     "emotion": {
    #                         "anger": 0.11452735,
    #                         "disgust": 0.9193782,
    #                         "fear": 0.055274334,
    #                         "joy": 0.0023334245,
    #                         "sadness": 0.06884794
    #                     },
    #                     "emotionMentions": [
    #                         {
    #                             "emotion": {
    #                                 "anger": 0.11452735,
    #                                 "disgust": 0.9193782,
    #                                 "fear": 0.055274334,
    #                                 "joy": 0.0023334245,
    #                                 "sadness": 0.06884794
    #                             },
    #                             "span": {
    #                                 "begin": 0,
    #                                 "end": 40,
    #                                 "text": "I feel disgusted just hearing about this"
    #                             }
    #                         }
    #                     ],
    #                     "target": ""
    #                 }
    #             ],
    #             "producerId": {
    #                 "name": "Ensemble Aggregated Emotion Workflow",
    #                 "version": "0.0.1"
    #             }
    #         }
    #     }    
    # """)
    def __init__(self):
        """constructor."""

    def emotion_detector(self, text_to_analyze):
        """method to detect emotion."""
        input_dict = { "raw_document": { "text": text_to_analyze }}
        response = requests.post(self.URL, json = input_dict, headers=self.HEADERS)
        return response.text

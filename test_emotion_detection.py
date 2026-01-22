"""Unit tests for EmotionDetection class"""
import unittest
import json
from EmotionDetection import EmotionDetection
from EmotionDetection import EmotionResponse


class TestEmotionDetection(unittest.TestCase):
    """Test cases for EmotionDetection class"""

    def setUp(self):
        """Set up test fixtures"""
        self.detector = EmotionDetection()

    def test_emotion_detector_joy(self):
        """Test emotion detection for joyful statement"""
        text = "I am glad this happened"
        result = self.detector.emotion_detector(text)
        result_json = json.loads(result)

        self.assertIn("emotionPredictions", result_json)
        emotions = result_json["emotionPredictions"][0]["emotion"]

        # Joy should be the highest emotion
        self.assertGreater(emotions["joy"], emotions["anger"])
        self.assertGreater(emotions["joy"], emotions["disgust"])
        self.assertGreater(emotions["joy"], emotions["fear"])
        self.assertGreater(emotions["joy"], emotions["sadness"])

    def test_emotion_detector_fear(self):
        """Test emotion detection for fearful statement"""
        text = "I am really afraid that this will happen"
        result = self.detector.emotion_detector(text)
        result_json = json.loads(result)

        self.assertIn("emotionPredictions", result_json)
        emotions = result_json["emotionPredictions"][0]["emotion"]

        # Fear should be the highest emotion
        self.assertGreater(emotions["fear"], emotions["anger"])
        self.assertGreater(emotions["fear"], emotions["disgust"])
        self.assertGreater(emotions["fear"], emotions["joy"])
        self.assertGreater(emotions["fear"], emotions["sadness"])

    def test_emotion_detector_anger(self):
        """Test emotion detection for angry statement"""
        text = "I am really mad about this"
        result = self.detector.emotion_detector(text)
        result_json = json.loads(result)

        self.assertIn("emotionPredictions", result_json)
        emotions = result_json["emotionPredictions"][0]["emotion"]

        # Anger should be the highest emotion
        self.assertGreater(emotions["anger"], emotions["disgust"])
        self.assertGreater(emotions["anger"], emotions["fear"])
        self.assertGreater(emotions["anger"], emotions["joy"])

    def test_emotion_detector_sadness(self):
        """Test emotion detection for sad statement"""
        text = "I am so sad about this"
        result = self.detector.emotion_detector(text)
        result_json = json.loads(result)

        self.assertIn("emotionPredictions", result_json)
        emotions = result_json["emotionPredictions"][0]["emotion"]

        # Sadness should be the highest emotion
        self.assertGreater(emotions["sadness"], emotions["anger"])
        self.assertGreater(emotions["sadness"], emotions["disgust"])
        self.assertGreater(emotions["sadness"], emotions["fear"])
        self.assertGreater(emotions["sadness"], emotions["joy"])

    def test_emotion_detector_disgust(self):
        """Test emotion detection for disgusted statement"""
        text = "I feel disgusted just hearing about this"
        result = self.detector.emotion_detector(text)
        result_json = json.loads(result)

        self.assertIn("emotionPredictions", result_json)
        emotions = result_json["emotionPredictions"][0]["emotion"]

        # Disgust should be the highest emotion
        self.assertGreater(emotions["disgust"], emotions["anger"])
        self.assertGreater(emotions["disgust"], emotions["fear"])
        self.assertGreater(emotions["disgust"], emotions["joy"])
        self.assertGreater(emotions["disgust"], emotions["sadness"])

    def test_emotion_detector_returns_json_string(self):
        """Test that emotion_detector returns a valid JSON string"""
        text = "I am glad this happened"
        result = self.detector.emotion_detector(text)

        # Should be a string
        self.assertIsInstance(result, str)

        # Should be valid JSON
        try:
            json.loads(result)
        except json.JSONDecodeError:
            self.fail("emotion_detector did not return valid JSON")

    def test_emotion_detector_has_all_emotions(self):
        """Test that all five emotions are present in the response"""
        text = "I am glad this happened"
        result = self.detector.emotion_detector(text)
        result_json = json.loads(result)

        emotions = result_json["emotionPredictions"][0]["emotion"]

        self.assertIn("anger", emotions)
        self.assertIn("disgust", emotions)
        self.assertIn("fear", emotions)
        self.assertIn("joy", emotions)
        self.assertIn("sadness", emotions)

    def test_emotion_response_dominant_emotion_joy(self):
        """Test EmotionResponse correctly identifies dominant emotion (joy)"""
        text = "I am glad this happened"
        result = self.detector.emotion_detector(text)
        response = EmotionResponse(result)

        emotions = response.emotions()
        self.assertIn("dominant_emotion", emotions)
        self.assertEqual(emotions["dominant_emotion"], "joy")

    def test_emotion_response_dominant_emotion_fear(self):
        """Test EmotionResponse correctly identifies dominant emotion (fear)"""
        text = "I am really afraid that this will happen"
        result = self.detector.emotion_detector(text)
        response = EmotionResponse(result)

        emotions = response.emotions()
        self.assertEqual(emotions["dominant_emotion"], "fear")

    def test_emotion_response_dominant_emotion_anger(self):
        """Test EmotionResponse correctly identifies dominant emotion (anger)"""
        text = "I am really mad about this"
        result = self.detector.emotion_detector(text)
        response = EmotionResponse(result)

        emotions = response.emotions()
        self.assertEqual(emotions["dominant_emotion"], "anger")

    def test_emotion_response_dominant_emotion_sadness(self):
        """Test EmotionResponse correctly identifies dominant emotion (sadness)"""
        text = "I am so sad about this"
        result = self.detector.emotion_detector(text)
        response = EmotionResponse(result)

        emotions = response.emotions()
        self.assertEqual(emotions["dominant_emotion"], "sadness")

    def test_emotion_response_dominant_emotion_disgust(self):
        """Test EmotionResponse correctly identifies dominant emotion (disgust)"""
        text = "I feel disgusted just hearing about this"
        result = self.detector.emotion_detector(text)
        response = EmotionResponse(result)

        emotions = response.emotions()
        self.assertEqual(emotions["dominant_emotion"], "disgust")

    def test_emotion_response_error_handling(self):
        """Test EmotionResponse sets all emotions to None for empty text"""
        text = ""
        result = self.detector.emotion_detector(text)
        response = EmotionResponse(result)

        emotions = response.emotions()

        # All emotions should be None when there's an error
        self.assertIsNone(emotions['anger'])
        self.assertIsNone(emotions['disgust'])
        self.assertIsNone(emotions['fear'])
        self.assertIsNone(emotions['joy'])
        self.assertIsNone(emotions['sadness'])
        self.assertIsNone(emotions['dominant_emotion'])


if __name__ == '__main__':
    unittest.main()
"""Unit tests for EmotionDetection class"""
import unittest
import json
from EmotionDetection import EmotionDetection

class TestEmotionDetection(unittest.TestCase):
    """Test cases for EmotionDetection class"""

    def setUp(self):
        """Set up test fixtures"""
        self.detector = EmotionDetection()

    def assert_emotition(self, text_to_analyze, dominant_emotion):
        """Common assert function"""
        self.detector.emotion_detector(text_to_analyze)
        self.assertIn("dominant_emotion", self.detector.emotions_json)
        self.assertEqual(self.detector.emotions_json["dominant_emotion"], dominant_emotion)

    def test_emotion_response_dominant_emotion_joy(self):
        """Test EmotionResponse correctly identifies dominant emotion (joy)"""
        text = "I am glad this happened"
        self.assert_emotition(text, 'joy')

    def test_emotion_response_dominant_emotion_anger(self):
        """Test EmotionResponse correctly identifies dominant emotion (anger)"""
        text = "I am really mad about this"
        self.assert_emotition(text, 'anger')

    def test_emotion_response_dominant_emotion_disgust(self):
        """Test EmotionResponse correctly identifies dominant emotion (disgust)"""
        text = "I feel disgusted just hearing about this"
        self.assert_emotition(text, 'disgust')

    def test_emotion_response_dominant_emotion_sadness(self):
        """Test EmotionResponse correctly identifies dominant emotion (sadness)"""
        text = "I am so sad about this"
        self.assert_emotition(text, 'sadness')

    def test_emotion_response_dominant_emotion_fear(self):
        """Test EmotionResponse correctly identifies dominant emotion (fear)"""
        text = "I am really afraid that this will happen"
        self.assert_emotition(text, 'fear')

if __name__ == '__main__':
    unittest.main()
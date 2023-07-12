"""dd"""
import unittest
import json
from emotion_detector import EmotionDetection
from sentiment_result import SentimentResult

class TestSentimentAnalysis(unittest.TestCase):
    """dd"""
    def setUp(self):
        """Setup method called before each test method."""
        self.sent_analyzer = SentimentAnalyzer()

    # Define the test method for sentiment analysis positive
    def test_analyze_sentiment_positive(self):
        """test."""
        result = self.sent_analyzer.analyze_sentiment("I am happy")
        sent_result = SentimentResult(result)
        self.assertEqual(sent_result.sentiment(), 'POSITIVE')

    # Define the test method for sentiment analysis negative
    def test_analyze_sentiment_negative(self):
        """test."""
        result = self.sent_analyzer.analyze_sentiment("I am very sad")
        sent_result = SentimentResult(result)
        self.assertEqual(sent_result.sentiment(), 'NEGATIVE')

    # Define the test method for bad result
    def test_analyze_sentiment_bad(self):
        """test."""
        print(self.sent_analyzer.analyze_sentiment("I am sad"))
        with self.assertRaises(Exception):
            self.sent_analyzer.analyze_sentiment("I am sad")
        
if __name__ == '__main__':
    unittest.main()
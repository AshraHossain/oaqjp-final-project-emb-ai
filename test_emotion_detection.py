# Create test_emotion_detection.py that calls the required application function to test it for the and dominant emotions.
from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        joy_emotion_test = emotion_detector('I am glad this happened')
        self.assertEqual(joy_emotion_test['dominant_emotion'], 'joy')
        anger_emotion_test = emotion_detector('I am really mad about this')
        self.assertEqual(anger_emotion_test['dominant_emotion'], 'anger')
        disgust_emotion_test = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(disgust_emotion_test['dominant_emotion'], 'disgust')
        sadness_emotion_test = emotion_detector('I am so sad about this')
        self.assertEqual(sadness_emotion_test['dominant_emotion'], 'sadness')
        fear_emotion_test = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(fear_emotion_test['dominant_emotion'], 'fear')

unittest.main()
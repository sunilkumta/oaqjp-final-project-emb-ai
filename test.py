import requests
from emotion_detection import EmotionDetection
from emotion_response import EmotionResponse
def main():
    emotion_detector = EmotionDetection()
    text = "I am really afraid that this will happen"
    result = emotion_detector.emotion_detector(text)
    emr = EmotionResponse(result)
    result = emr.emotions()
    print(emr.emotions_info())

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", str(e))


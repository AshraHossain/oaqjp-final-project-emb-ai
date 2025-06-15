 # Import the requests & json libraries
import requests
import json

def emotion_detector(text_to_analyse):
     # URL of the Emotion Predict function
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    input_json = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Sending a POST request to the API
    response = requests.post(URL, json = input_json, headers=header)
    
    #Convert the response text into a dictionary using the json library functions.
    formatted_response = json.loads(response.text)

    #Extract the required set of emotions, including anger, disgust, fear, joy and sadness, along with their scores
    emotions = {}
    if 'emotionPredictions' in formatted_response and formatted_response['emotionPredictions']:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        
    # Modify the emotion_detector function to return in output format specified
    return{
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
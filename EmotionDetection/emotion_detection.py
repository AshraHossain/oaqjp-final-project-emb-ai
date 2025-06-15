 # Import the requests & json libraries
import requests
import json

def emotion_detector(text_to_analyse):
    # Handle blank entries from users
    if not text_to_analyse.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # URL of the Emotion Predict function
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Constructing the request payload in the expected format
    input_json = { "raw_document": { "text": text_to_analyse } }
    
    # Custom header specifying the model ID
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the API
    response = requests.post(URL, json=input_json, headers=header)

    # Handle API errors (status_code 400)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    #Convert the response text into a dictionary using the json library functions.
    formatted_response = json.loads(response.text)

    # Extract emotions safely
    emotions = {}
    dominant_emotion = None
    if 'emotionPredictions' in formatted_response and formatted_response['emotionPredictions']:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        if emotions:  # Ensure there are emotions before finding the dominant one
            dominant_emotion = max(emotions, key=emotions.get)

    # Return structured response
    return {
        'anger': emotions.get('anger', None),
        'disgust': emotions.get('disgust', None),
        'fear': emotions.get('fear', None),
        'joy': emotions.get('joy', None),
        'sadness': emotions.get('sadness', None),
        'dominant_emotion': dominant_emotion
    }

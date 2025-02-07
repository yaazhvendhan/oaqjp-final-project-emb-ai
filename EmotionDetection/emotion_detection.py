import requests
import json

# Watson NLP API Endpoint
URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    """Function to detect emotions in text using Watson NLP API."""
    
    # Check for blank input
    if not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    
    # Prepare the data for the API request
    data = {"raw_document": {"text": text_to_analyze}}
    
    # Send the POST request to the Watson NLP API
    response = requests.post(URL, headers=HEADERS, json=data)
    
    # Check if the API request is successful
    if response.status_code == 200:
        emotions = json.loads(response.text)  # Convert response to dictionary
        emotion_scores = emotions["emotionPredictions"][0]["emotion"]  # Extract emotion scores

        # Identify the dominant emotion
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Return the formatted output
        return {
            "anger": emotion_scores["anger"],
            "disgust": emotion_scores["disgust"],
            "fear": emotion_scores["fear"],
            "joy": emotion_scores["joy"],
            "sadness": emotion_scores["sadness"],
            "dominant_emotion": dominant_emotion
        }
    else:
        # Return the error message with status code in case of failure
        return {
            "error": "API request failed",
            "status_code": response.status_code
        }

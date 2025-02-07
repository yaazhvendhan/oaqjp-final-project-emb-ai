import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}

    # Sending the request to the Watson NLP API
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        # Convert response text into dictionary
        response_data = json.loads(response.text)

        # Extract emotions and their scores
        emotions = response_data.get("emotion_predictions", [{}])[0].get("emotion", {})

        # Find the dominant emotion (emotion with the highest score)
        dominant_emotion = max(emotions, key=emotions.get) if emotions else "unknown"

        # Return the formatted dictionary
        return {
            'anger': emotions.get('anger', 0),
            'disgust': emotions.get('disgust', 0),
            'fear': emotions.get('fear', 0),
            'joy': emotions.get('joy', 0),
            'sadness': emotions.get('sadness', 0),
            'dominant_emotion': dominant_emotion
        }
    else:
        return {"error": f"API request failed with status code {response.status_code}"}

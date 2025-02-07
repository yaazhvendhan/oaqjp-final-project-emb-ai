from flask import Flask, jsonify, request
from EmotionDetection import emotion_detection

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector():
    # Extract the statement from the JSON body
    data = request.get_json()
    statement = data.get('statement', '')

    # Process the statement using emotion detection
    emotions = emotion_detection.emotion_detector(statement)

    # Prepare the result
    dominant_emotion = max(emotions, key=emotions.get)
    response = {
        **emotions,
        'dominant_emotion': dominant_emotion
    }

    # Return the result in JSON format
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

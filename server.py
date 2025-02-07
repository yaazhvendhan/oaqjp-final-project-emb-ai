"""
Flask application for Emotion Detection API.
"""

from flask import Flask, jsonify, request
from EmotionDetection import emotion_detection

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector():
    """
    API endpoint to analyze emotions in a given statement.
    Returns a JSON response with emotion scores and the dominant emotion.
    """
    # Extract the statement from the JSON body
    data = request.get_json()
    statement = data.get('statement', '').strip()

    # Check for blank input
    if not statement:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    # Process the statement using the emotion detection function
    emotions = emotion_detection.emotion_detector(statement)

    # Check if dominant emotion is None (invalid text)
    if emotions.get("dominant_emotion") is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    # Return the result as a JSON response
    return jsonify(emotions)

if __name__ == '__main__':
    app.run(debug=True)

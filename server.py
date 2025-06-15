''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["GET", "POST"])
def emo_detector():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    if request.method == "POST":
        data = request.get_json()
        text_to_analyze = data.get("text", "")
    else:
        text_to_analyze = request.args.get("textToAnalyze", "")

    # Ensure blank input is handled correctly
    if not text_to_analyze.strip():
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    # Call 'emotion_detector' function
    response = emotion_detector(text_to_analyze)

    # Error handling for None values in the response
    if not response["dominant_emotion"] or all(value is None for value in response.values()):
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    # Return a properly formatted JSON response
    return jsonify({
        "message": (
            f"For the given statement, the system response is 'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
            f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}."
        )
    })

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5099)

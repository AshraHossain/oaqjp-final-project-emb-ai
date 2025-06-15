from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["GET", "POST"])
def emo_detector():
    """
    Handles emotion detection requests. Supports both GET and POST methods.
    - GET: Accepts 'textToAnalyze' as a query parameter.
    - POST: Accepts a JSON body with 'text' as the key.
    Returns a formatted string response with detected emotions.
    """
    if request.method == "POST":
        data = request.get_json()
        if not data or "text" not in data:
            return "Invalid text! Please try again!", 400  # Handle missing input
        text_to_analyze = data["text"]
    else:  # Handling GET requests
        text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze:
        return "Invalid text! Please try again!", 400  # Handle missing input

    response = emotion_detector(text_to_analyze)

    # Format the response string exactly as required
    formatted_response = (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return formatted_response  # Returning the formatted string response

@app.route("/")
def render_index_page():
    """
    Renders the index page for the application.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

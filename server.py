'''This application is using emotion detection to evaluate sentences
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Instantiate Flask functionality
app = Flask("Emotion Detection Application")

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main page
    '''
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detection():
    ''' This function formats the output after calling the detection
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    r = emotion_detector(text_to_analyze)

    if r['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    text = f'''
        For the given statement, the system response is 'anger': {r["anger"]}, 
        'disgust': {r["disgust"]}, 'fear': {r["fear"]}, 'joy': {r["joy"]} and 
        'sadness': {r["sadness"]}. The dominant emotion is {r["dominant_emotion"]}.
    '''

    return text

# Starting the server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

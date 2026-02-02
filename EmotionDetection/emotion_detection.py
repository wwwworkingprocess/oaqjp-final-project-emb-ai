import requests  
import json

def emotion_detector(text_to_analyze):
    # Error handling: In case the user input is blank
    if (len(text_to_analyze) == 0):
        return {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy" : None, 
            "sadness": None,
            "dominant_emotion":None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  

    # Create a dictionary with the text to be analyzed
    payload = { "raw_document": { "text": text_to_analyze } }  

    # Set the headers required for the API request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = payload, headers=headers)

    # Error handling: In case the server returned 400
    if (response.status_code == 400):
        return {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy" : None, 
            "sadness": None,
            "dominant_emotion":None
        }

    formatted_response = json.loads(response.text)
    prediction = formatted_response["emotionPredictions"][0]

    if (prediction):
        emotion = prediction["emotion"]
        result = {
            "anger": emotion["anger"], 
            "disgust": emotion["disgust"], 
            "fear": emotion["fear"], 
            "joy" : emotion["joy"], 
            "sadness": emotion["sadness"]
        }

        result["dominant_emotion"] = max(result, key=result.get)

        return result
import requests

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        response = response.json()
        emotions = response['emotionPredictions'][0]['emotion']
        highest = 0
        dominant_emotion = ''
        for emotion, value in emotions.items():
            if value > highest:
                highest = value
                dominant_emotion = emotion
        return {
            'anger': emotions['anger'],
            'disgust' : emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness' : emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
    else:
        print(f"Error {response.status_code}: {response.text}")

# print(emotion_detector('I am so happy I am doing this'))
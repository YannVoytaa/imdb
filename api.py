import requests
from apikey import API_KEY 

from fastapi import FastAPI

app = FastAPI()


@app.post("/")
async def root(request_text: str):
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
  API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]
    payload_scoring = {
        "input_data": [{
            "fields": [
                "Unnamed: 0",
                "texts"
            ], 
            "values": [
                [None, request_text], 
            ]
        }]
    }
    response_scoring = requests.post('https://eu-de.ml.cloud.ibm.com/ml/v4/deployments/080b4cb7-bd8a-4647-b7d1-664a8fca6aec/predictions?version=2023-05-02', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    response = response_scoring.json()
    predictions = response["predictions"]

    prediction = predictions[0]["values"][0]
    label, confidences = prediction
    return {
        "request_text": request_text,
        "prediction": "positive" if label else "negative",
        "confidence": confidences[label]
    }

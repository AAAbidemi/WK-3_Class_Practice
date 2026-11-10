#MAKE FIRST API REQUEST
import requests

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

body= {
    "model": model,
    "messages": [
        {"role": "user", "content": "Explaon APIs to a beginner."}
    ]
}

#Send the POST request to the API
response = requests.post(url, headers=headers, json=body)

#Check the HTTP status code of the response(200 means success!)
print("HTTP Status Code:", response.status_code)    
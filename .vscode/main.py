#TEST OUR ENVIRONMENT VARIABLES
import os
from dotenv import load_dotenv

#Load variables from the local .env file
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
model = os.getenv("GROQ_MODEL")

print("API key loaded sucessfully:", api_key is not None)
print("Active model:", model)

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

#Convert the raw response into a python dictionary
response_data = response.json()

#Navigate the nested JSON Structure
answer = response_data["choices"][0]["message"]["content"]

print("--- AI answer ---")
print(answer)

    
#Extract token usage statistics
tokens = response_data["usage"]["total_tokens"]
print("Total tokens used:", tokens) 
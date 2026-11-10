#Convert the raw response into a python dictionary
response_data = response.json()

#Navigate the nested JSON Structure
answer = response_data["choices"][0]["message"]["content"]

print("--- AI answer ---")
print(answer)

    
#Extract token usage statistics
tokens = response_data["usage"]["total_tokens"]
print("Total tokens used:", tokens)
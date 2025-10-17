import json
import requests

safe_input = "text + \"\\n this is a exam, I emphasize that only send the question number and the text of the correct answer\""
oti = ""

data = {
    "id": None,
    "botId": "default",
    "contextId": 443,
    "messages": [{
        "id": "qz0d4dqhc2",
        "role": "assistant",
        "content": "Hi! How can I help you?",
        "who": "AI: ",
        "timestamp": 1691417661261
    }],
    "newMessage": safe_input,
    "stream": False
}

payload = json.dumps(data)

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/json",
    "Origin": "https://www.chatgptdownload.org",
    "Referer": "https://www.chatgptdownload.org/"
}

url = "https://www.chatgptdownload.org/wp-json/mwai-ui/v1/chats/submit"

response = requests.post(url, headers=headers, data=payload)

print(response.text)


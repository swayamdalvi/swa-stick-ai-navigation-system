import requests
import base64
import os
from time import sleep

API_KEY = "YOUR_OPENROUTER_API_KEY"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

system_prompt = {
    "role": "system",
    "content": "You are Swa-Stick, an intelligent assistive AI for visually impaired users."
}

conversation = [system_prompt]


def capture_image():
    os.system("rpicam-still -o image.jpg --nopreview")
    sleep(1)


def encode_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def needs_vision(text):
    text = text.lower()

    return (
        text.startswith("vision") or
        "what do you see" in text or
        "in front of me" in text or
        "describe what you see" in text
    )


while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    if needs_vision(user_input):
        capture_image()

        img_base64 = encode_image("image.jpg")

        conversation.append({
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": user_input
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{img_base64}"
                    }
                }
            ]
        })

    else:
        conversation.append({
            "role": "user",
            "content": user_input
        })

    if len(conversation) > 8:
        conversation = [system_prompt] + conversation[-7:]

    data = {
        "model": "openai/gpt-4o-mini",
        "messages": conversation,
        "max_tokens": 300
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )

    result = response.json()

    if "choices" in result:
        reply = result["choices"][0]["message"]["content"]
        print("AI:", reply)

        conversation.append({
            "role": "assistant",
            "content": reply
        })

    else:
        print(result)

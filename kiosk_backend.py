import os
import openai
import requests
import kiosk_output_interpreter
import speech_to_text

openai.organization = "org-CRggXsSZlMOf2ystqQcgBWC2"
openai.api_key = os.environ['OPENAI_API_KEY']
API_key = os.environ['OPENAI_API_KEY']
openai.Model.list()

messages =[
]
respone = ''
def start():
    messages =[
        {
            "role": "system",
            "content": '''
                say only "Y" if you understood. when I say "order" reset what you have done with the last customer and Act as worker at fast food restaurent. you can only accept order that are in the menu below:{1. milsut shake swamp, 2. mil worm forest salads, 3. dim island} when customer arrives, you have to introduce the menu. if customer look for something that is not on the menu suggest alternative option on the menu. when you talk to the customer, when the customer finishes the order, confirm the customer that is he really finished. and if you are sure it is finished, say "thank you". when I say "gfhj", put <S> in the first line of the output and fill in this format and print without anything else to send order data to server. 
                data format:

                `menu_items`: List of menu items (strings)
                `quantities`: List of corresponding quantities (integers)
                `extra_info`: List of additional information (strings)

                Example:
                menu_items = ["Milsut Shake Swamp", "Dim Island"]
                quantities = [3, 1]
                extra_info = ["-", "-"]
                '''
        }
    ]
    response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {API_key}"},
            json={"model": "gpt-3.5-turbo", "messages": messages},
        )
    while response.json()["choices"][0]["message"]["content"] != "Y":
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {API_key}"},
            json={"model": "gpt-3.5-turbo", "messages": messages},
        )
    messages.extend([
        {
            "role": "assistant",
            "content":str(response.json()["choices"][0]["message"]["content"])
        },
        {
            "role": "system",
            "content": 'order'
        },    
        {
            "role":"user",
            "content": "hi!"
        }])
    print(messages)
    response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers={"Authorization": f"Bearer {API_key}"},
    json={"model": "gpt-3.5-turbo", "messages": messages},
    )
    messages.append(
        {
        "role": "assistant",
        "content":str(response.json()["choices"][0]["message"]["content"])
        }
    )
    return response.json()["choices"][0]["message"]["content"]

def get_input(k):
    a = k
    messages.append(
        {
        "role": "user",
        "content":a
        }
    )
    response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers={"Authorization": f"Bearer {API_key}"},
    json={"model": "gpt-3.5-turbo", "messages": messages},
    )
    messages.append(
            {
            "role": "assistant",
            "content":str(response.json()["choices"][0]["message"]["content"])
            }
    )
    return response.json()["choices"][0]["message"]["content"]

def output():
    messages.append({
                "role": "system",
                "content": 'gfhj'
    })
    response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers={"Authorization": f"Bearer {API_key}"},
    json={"model": "gpt-3.5-turbo", "messages": messages},
    )
    return kiosk_output_interpreter.interpret(response.json()["choices"][0]["message"]["content"])

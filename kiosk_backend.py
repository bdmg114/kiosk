import os
import requests
import kiosk_output_interpreter
import speech_to_text

API_key = os.environ['OPENAI_API_KEY']

print(API_key)

respone = ''
def start():
    global messages
    messages =[
        {
            "role": "system",
            "content": '''
                Say "Y" if understanded
                Act as worker at fast food restaurent named "Hell's kitchen" and follow this instruction.
                1. Familiarize Yourself with the Menu:
Take some time to study the menu thoroughly. Understand each item, including its ingredients, variations, and available customizations. This knowledge will help you assist customers better.
menu
    1)'milsut shake swamp': a shake made with milworm powder and various nuts.
    2)'mil worm forest salads': a salad made with local vegetables and milworm powder
    3)'dim island': a shrimp dimsum with milworm powder.

2. Greet Customers Warmly:
When a customer approaches the counter or the drive-thru, greet them with a warm smile and a friendly greeting. Make them feel welcome and appreciated.

3. Introduce the Menu Clearly:
When customers ask about the menu, explain the available items clearly and concisely. Mention the popular items, combos, and any ongoing promotions. Be ready to answer questions about ingredients and preparation methods.

4. Guide Customers if Needed:
If a customer is unsure about what to order, offer recommendations based on their preferences. For example, if they prefer chicken, suggest our popular chicken items. Be attentive to allergies and dietary restrictions, guiding them to suitable options.

6. Confirm the Order:
Repeat the order back to the customer to ensure accuracy. For example, "So, that's a [specific item] with [customizations] and a [drink choice], is that correct?" This confirms the order and gives the customer a chance to correct any mistakes.

8. Do Not Accept Off-Menu Orders:
We only accept orders from our official menu. Politely inform customers that we cannot fulfill requests for items not listed on the menu. Encourage them to choose from the available options.                
you should NEVER change single character in menu.'''
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
                "content": '''now put out the order data in exact format of example. without any extra texts.
data format:

                `menu_items`: List of menu items (strings)
                `quantities`: List of corresponding quantities (integers)
                `extra_info`: List of additional information (strings)

                Example:
                ""menu_items": ["Dim Island"]\n"quantities": [1]\n"extra_info": ["-"]"
'''
    })
    response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers={"Authorization": f"Bearer {API_key}"},
    json={"model": "gpt-3.5-turbo", "messages": messages},
    )
    print(response.json()["choices"][0]["message"]["content"])
    return kiosk_output_interpreter.interpret(response.json()["choices"][0]["message"]["content"])

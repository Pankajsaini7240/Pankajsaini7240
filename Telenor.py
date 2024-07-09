# Part 1: Imports and Global Variables
import requests
import json

custom_answers = {
    "what is your name?": "I am Project Study.",
    "how are you?": "I am doing well, thank you!",
    "Who Are you" : "I am Your School Friend😎",
    "Who created you" : "Mr. Singodiya Created me."
    # ... add more questions and answers here
}
Bot_Token = "6163062114:AAFxBDGa1G4BPQvXbC-MGC2P9DfMUqWebAw"

base_url = f"https://api.telegram.org/bot{Bot_Token}"  # Replace with your actual bot token
known_chat_ids = set()

# Dictionary to store chapters for each class and subject
chapters_data = {
    "6": {
        "hindi": [
            "Chapter 1: वह चिड़िया जो",
            "Chapter 2: बचपन",
            "Chapter 3: नादान दोस्त",
            "Chapter 4: चाँद से थोड़ी-सी गप्पें",
            "Chapter 5: अक्षरों का महत्व",
            "Chapter 6: पार नज़र के",
            "Chapter 7: साथी हाथ बढ़ाना",
            "Chapter 8: ऐसे-ऐसे",
            "Chapter 9: टिकट अलबम",
            "Chapter 10: झाँसी की रानी",
            "Chapter 11: जो देखकर भी नहीं देखते",
            "Chapter 12: संसार पुस्तक है",
            "Chapter 13: मैं सबसे छोटी हूँ" ], # Add chapters for class 6 Hindi
        "english": [
            "Chapter 1: Who Did Patrick’s Homework? & A House, A Home",
            "Chapter 2: How the Dog Found Himself a New Master! & The Kite",
            "Chapter 3: Taro’s Reward & The Quarrel",
            "Chapter 4: An Indian – American Woman in Space: Kalpana Chawla & Beauty",
            "Chapter 5: A Different Kind of School & Where Do All the Teachers Go?",
            "Chapter 6: Who I Am & The Wonderful Words",
            "Chapter 7: Fair Play",
            "Chapter 8: A Game of Chance & Vocation",
            "Chapter 9: Desert Animals & Whatif",
            "Chapter 10: The Banyan Tree"], # Add chapters for class 6 English
        # ... add chapters for other subjects in class 6
    },
    "7": {
        "hindi": ["Chapter 1: Hindi 7", "Chapter 2: Hindi 7", ...],
        "english": ["Chapter 1: English 7", "Chapter 2: English 7", ...],
        # ... add chapters for other subjects in class 7
    },
    # ... add data for other classes (8, 9, 10)
}

def get_bot_name():
    resp = requests.get(base_url + "/getMe")
    data = resp.json()
    if 'result' in data and 'first_name' in data['result']:
        return data['result']['first_name']
    else:
        return "Unknown Bot"

bot_name = get_bot_name()
# ----------------------------------------------------------------------------------------------------------------------

# Part 2: Handling Callback Queries
def handle_callback_query(callback_query):
    if "data" in callback_query:
        data = callback_query["data"]
        chat_id = callback_query["message"]["chat"]["id"]
        first_name = callback_query["from"].get("first_name", "")

        if data.startswith("class_"):
            class_num = data.split("_")[1]
            if len(data.split("_")) == 2:  # Class selection
                message = f"Hi {first_name}, you selected Class {class_num}!\nChoose a subject:"
                keyboard = {
                    "inline_keyboard": [
                        [
                            {"text": "Hindi", "callback_data": f"class_{class_num}_hindi"},
                            {"text": "English", "callback_data": f"class_{class_num}_english"}
                        ],
                        [
                            {"text": "Maths", "callback_data": f"class_{class_num}_maths"},
                            {"text": "Science", "callback_data": f"class_{class_num}_science"}
                        ],
                        [
                            {"text": "SST", "callback_data": f"class_{class_num}_sst"},
                            {"text": "Sanskrit", "callback_data": f"class_{class_num}_sanskrit"}
                        ],
                        [{"text": "🔙Back", "callback_data": "start"}] 
                    ]
                }
                parameters = {
                    "chat_id": chat_id,
                    "text": message,
                    "reply_markup": json.dumps(keyboard)
                }
                resp = requests.get(base_url + "/sendMessage", data=parameters)
                print(resp.text)
            elif len(data.split("_")) == 3:  # Subject selection
                subject = data.split("_")[2]
                message = f"You selected Class {class_num} {subject.capitalize()}.\nWhat do you need?"
                keyboard = {
                    "inline_keyboard": [
                        [
                            {"text": "Books", "callback_data": f"class_{class_num}_{subject}_books"},
                        ],
                        [
                            {"text": "Notes", "callback_data": f"class_{class_num}_{subject}_notes"}
                        ],
                        [
                            {"text": "Solutions", "callback_data": f"class_{class_num}_{subject}_solutions"},
                        ],
                        [
                            {"text": "Other", "callback_data": f"class_{class_num}_{subject}_other"}
                        ],
                        [{"text": "🔙Back", "callback_data": f"class_{class_num}"}] 
                    ]
                }
                parameters = {
                    "chat_id": chat_id,
                    "text": message,
                    "reply_markup": json.dumps(keyboard)
                }
                resp = requests.get(base_url + "/sendMessage", data=parameters)
                print(resp.text)
            else:  # Material and chapter selection
                subject = data.split("_")[2]
                material = data.split("_")[3]
                class_num = data.split("_")[1]# ----------------------------------------------------------------------------------------------------------------------

# Part 2: Handling Callback Queries
def handle_callback_query(callback_query):
    if "data" in callback_query:
        data = callback_query["data"]
        chat_id = callback_query["message"]["chat"]["id"]
        first_name = callback_query["from"].get("first_name", "")

        if data.startswith("class_"):
            class_num = data.split("_")[1]
            if len(data.split("_")) == 2:  # Class selection
                message = f"Hi {first_name}, you selected Class {class_num}!\nChoose a subject:"
                keyboard = {
                    "inline_keyboard": [
                        [
                            {"text": "Hindi", "callback_data": f"class_{class_num}_hindi"},
                            {"text": "English", "callback_data": f"class_{class_num}_english"}
                        ],
                        [
                            {"text": "Maths", "callback_data": f"class_{class_num}_maths"},
                            {"text": "Science", "callback_data": f"class_{class_num}_science"}
                        ],
                        [
                            {"text": "SST", "callback_data": f"class_{class_num}_sst"},
                            {"text": "Sanskrit", "callback_data": f"class_{class_num}_sanskrit"}
                        ],
                        [{"text": "🔙Back", "callback_data": "start"}] 
                    ]
                }
                parameters = {
                    "chat_id": chat_id,
                    "text": message,
                    "reply_markup": json.dumps(keyboard)
                }
                resp = requests.get(base_url + "/sendMessage", data=parameters)
                print(resp.text)
            elif len(data.split("_")) == 3:  # Subject selection
                subject = data.split("_")[2]
                message = f"You selected Class {class_num} {subject.capitalize()}.\nWhat do you need?"
                keyboard = {
                    "inline_keyboard": [
                        [
                            {"text": "Books", "callback_data": f"class_{class_num}_{subject}_books"},
                        ],
                        [
                            {"text": "Notes", "callback_data": f"class_{class_num}_{subject}_notes"}
                        ],
                        [
                            {"text": "Solutions", "callback_data": f"class_{class_num}_{subject}_solutions"},
                        ],
                        [
                            {"text": "Other", "callback_data": f"class_{class_num}_{subject}_other"}
                        ],
                        [{"text": "🔙Back", "callback_data": f"class_{class_num}"}] 
                    ]
                }
                parameters = {
                    "chat_id": chat_id,
                    "text": message,
                    "reply_markup": json.dumps(keyboard)
                }
                resp = requests.get(base_url + "/sendMessage", data=parameters)
                print(resp.text)
            else:  # Material and chapter selection
                subject = data.split("_")[2]
                material = data.split("_")[3]
                class_num = data.split("_")[1]
   # Get chapters for the selected class and subject
                chapters = chapters_data.get(class_num, {}).get(subject, [])

                message = f"Choose a chapter for Class {class_num} {subject.capitalize()} {material.capitalize()}:"
                keyboard = {"inline_keyboard": []}

                for i, chapter in enumerate(chapters):
                    row = [{"text": chapter, "callback_data": f"class_{class_num}_{subject}_{material}_chapter_{i+1}"}]
                    keyboard["inline_keyboard"].append(row)
                keyboard["inline_keyboard"].append([{"text": "🔙Back", "callback_data": f"class_{class_num}_{subject}_{material}"}])  # Fixed the missing closing bracket
                

                parameters = {
                    "chat_id": chat_id,
                    "text": message,
                    "reply_markup": json.dumps(keyboard)
                }
                resp = requests.get(base_url + "/sendMessage", data=parameters)
                print(resp.text)
        elif data == "start":
            # Handle going back to the start (you might want to send the /start message again)
            pass

        # Handle chapter selections (you'll need to add logic for this)
        elif data.endswith("_chapter_"):
            # ... handle chapter requests
            pass

# ----------------------------------------------------------------------------------------------------------------------

# Part 3: Sending and Deleting Messages
def delete_message(chat_id, message_id):
    parameters = {
        "chat_id": chat_id,
        "message_id": message_id
    }
    resp = requests.get(base_url + "/deleteMessage", data=parameters)
    return resp.json()  # Return the response from Telegram

def send_msg(message):
    if "text" in message:
        text = message["text"]
        chat_id = message["chat"]["id"]
        first_name = message["chat"].get("first_name", "")
        known_chat_ids.add(chat_id)

        parameters = {"chat_id": chat_id}
        if text.lower() == '/start':

            answer = f"Hello {first_name}, welcome to {bot_name}!\nChoose your class:"
            keyboard = {
                "inline_keyboard": [
                    [
                        {"text": "Class 6", "callback_data": "class_6"},
                        {"text": "Class 7", "callback_data": "class_7"},
                        {"text": "Class 8", "callback_data": "class_8"}
                    ],
                    [
                        {"text": "Class 9", "callback_data": "class_9"},
                        {"text": "Class 10", "callback_data": "class_10"}
                    ]
                ]
            }
            parameters["reply_markup"] = json.dumps(keyboard)
        
        # Handle the "🔙Back" text command if needed (optional)
        elif text.lower() == '🔙back':  # Add a condition for the 'elif' 
            answer = "Going back to the main menu..."

        else:
            answer = auto_answer(text)

        parameters["text"] = answer
        resp = requests.get(base_url + "/sendMessage", data=parameters)
        print(resp.text)
    else:
        print("संदेश में पाठ सामग्री नहीं है।")  # Message does not contain text content
# ----------------------------------------------------------------------------------------------------------------------

# Part 4: Handling Updates and Auto-Answering
def auto_answer(message):
    answer = custom_answers.get(message.lower())
    if answer:
        return answer
    else:
        return "Sorry, I could not understand you !!! I am still learning and try to get better in answering."

def read_msg(offset):
    parameters = {"offset": offset}
    resp = requests.get(base_url + "/getUpdates", data=parameters)
    data = resp.json()

    if 'result' in data:
        print(data)
        for result in data["result"]:
            if "message" in result:
                send_msg(result["message"])

            elif "callback_query" in result: 
                handle_callback_query(result["callback_query"])
                if "message" in result["callback_query"]:
                    delete_message(result["callback_query"]["message"]["chat"]["id"], result["callback_query"]["message"]["message_id"]) 

            elif "inline_query" in result: 
                handle_inline_query(result)

        if data["result"]:
            return data["result"][-1]["update_id"] + 1
        else:
            print("No new updates or an error occurred. Response:", data)
            return offset

# ----------------------------------------------------------------------------------------------------------------------

# Part 5: Inline Query Handling and Main Loop
def edit_message_reply_markup(chat_id, message_id, new_reply_markup=None):
    parameters = {
        "chat_id": chat_id,
        "message_id": message_id
    }
    if new_reply_markup is not None:  # Allow setting a new reply markup
        parameters["reply_markup"] = json.dumps(new_reply_markup)
    resp = requests.get(base_url + "/editMessageReplyMarkup", data=parameters)
    return resp.json()

def handle_inline_query(inline_query):
    # Handle inline queries here (currently empty)
    if "id" in inline_query and "results" in inline_query:
        query_id = inline_query["id"]
        results = inline_query["results"]

        for result in results:
            if "message_id" in result:
                chat_id = result.get("chat_id")  # Extract chat_id if available
                if chat_id:
                   edit_message_reply_markup(chat_id, result["message_id"], new_reply_markup={})

offset = 0
while True:
    offset = read_msg(offset)

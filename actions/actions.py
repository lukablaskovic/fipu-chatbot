import os
from dotenv import load_dotenv

from typing import Any, Text, Dict, List
import pandas as pd
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import json

load_dotenv()

class unipuAPI(object):

    def __init__(self):
        self.db = pd.read_json("json/praksa_poduzeca_zadaci.json")

    def fetch_data(self):
        return self.db

    def format_data(self, df, header=True) -> Text:
        return df.to_csv(index=False, header=header)

unipu_API = unipuAPI()


class ActionShowData(Action):

    def name(self) -> Text:
        return "action_show_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        data = unipu_API.fetch_data()

        data_list = data["lista_poduzeca"]
        readable = [(item["id"], item["name"]) for item in data_list]

        message = "\n".join([f"ID: {item[0]}, Name: {item[1]}" for item in readable])

        dispatcher.utter_message(text=f"Izvolite listu dostupnih poduzeća za obavljanje prakse:\n\n{message}")

        return [SlotSet("results", readable)]


class ChatGPT(object):

    def __init__(self):
        self.url = "https://api.openai.com/v1/chat/completions"
        self.model = "gpt-3.5-turbo"
        self.headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('OPEN_AI_API')}"
        }
        self.prompt = "Answer the following request in Croatian language, based on the JSON data shown." \
            "If asked for tasks (zadatak in Croatian) then please do following: First check whether provided company has available tasks. Second, if you found tasks, then provide details about them." \
            "If you cannot find an answer, please say so'.\n\n"
        
    def ask(self, previous_results, question):
        
        data = unipu_API.fetch_data()
        s_data = unipu_API.format_data(data, header=False)
        print(s_data)   
        
        content  = self.prompt + "\n\n" + s_data + "\n\n" + question
        body = {
            "model":self.model, 
            "messages":[{"role": "user", "content": content}]
        }
        result = requests.post(
            url=self.url,
            headers=self.headers,
            json=body,
        )
        response = result.json()
        print(response)
        return result.json()["choices"][0]["message"]["content"]
    
chatGPT = ChatGPT()
print(chatGPT.headers)
class ActionDetail(Action):
    def name(self) -> Text:
        return "action_get_detail"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        previous_results = tracker.get_slot("results")
        question = tracker.latest_message["text"]
        answer = chatGPT.ask(previous_results, question)
        dispatcher.utter_message(text = answer)


# Import necessary Rasa libraries and modules
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json

from typing import Any, Dict, List, Text

class ActionSearchCompanies(Action):
    def name(self) -> Text:
        return "action_search_companies"

    def run(
        self, 
        dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        companies = search_for_companies()
        #print(companies)
      
        if companies:
            company_names = "\n".join([f"{i+1}. {company['name']}" for i, company in enumerate(companies)])
            dispatcher.utter_message(text=f"Popis poduzeća za obavljanje studentske prakse:\n{company_names}")
       
        else:
            dispatcher.utter_message(text="Žao mi je, ne mogu pronaći ni jedno poduzeće za studentsku praksu.")
            
        return []


def search_for_companies():
  f = open("json_data/lista_poduzeca_praksa.json")
  companies = json.load(f)
  companies_list = [comp for comp in companies["lista_poduzeca"]]
  return companies_list

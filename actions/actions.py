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

class ActionSearchProjects(Action):
    def name(self) -> Text:
        return "action_show_projects"
    
    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string (company_id) is an integer."""

        try:
            int(string)
            return True
        except ValueError:
            return False
    
    def validate_company_id(
        self,
        id: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate company_id value."""
        company_id = int(id)
        if company_id in get_companies_id():
            return {"company_id": company_id}
        else:
            return {"company_id": None}

    def run(
        self, 
        dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        
        company_id = tracker.get_slot("company_id")
        validated_id = self.validate_company_id(company_id, dispatcher, tracker, domain)["company_id"]
        print(validated_id)
        if(validated_id):
            projects = search_company_projects(company_id)
            if projects:
                project = "\n".join([f"\nZadatak {project['id']}:\n Kontakt email: {project['kontakt_email']}\n Opis zadatka: {project['opis_zadatka']}\n Preferirane tehnologije: {project['preferirane_tehnologije']}\n Preferencije za studenta: {project['student_preferencije']}\n Potrebno je imati: {project['potrebno_imati']}\n Trajanje: {project['trajanje_h']} sati\n Lokacija: {project['lokacija']}\n Željeno okvirno vrijeme početka: {project['okvirno_vrijeme_pocetka']}\n Angažman FIPU: {project['angazman_fipu']}\n Napomena: {project['napomena']}\n " for project in projects])
                dispatcher.utter_message(text=f"Popis zadataka za odabranu tvrtku:\n\n{project}")
            else:
                dispatcher.utter_message(text="Za odabranu tvrtku nema definiranih zadataka. Međutim, možeš obavijestiti tvrtku da ga definira na: http://bit.ly/fipu-praksa-prijava-zadatka")
        else:
            dispatcher.utter_message(text="Unio si nepostojeći ID tvrtke. Molim te provjeri ponovo ili kontaktiraj administratora.")
        return []

def search_for_companies():
  f = open("json_data/praksa_poduzeca_zadaci.json")
  companies = json.load(f)
  companies_list = [comp for comp in companies["lista_poduzeca"]]
  return companies_list

def get_companies_id():
    f = open("json_data/praksa_poduzeca_zadaci.json")
    companies = json.load(f)
    companies_id = [company["id"] for company in companies["lista_poduzeca"]]
    return companies_id

def search_company_projects(id):
    f = open("json_data/praksa_poduzeca_zadaci.json")
    companies = json.load(f)
    for company in filter(lambda c : c["id"] == int(id), companies["lista_poduzeca"]):
        return company["zadaci"] if company["zadaci"] else None
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
    jobs = [
    {
      "id": 0,
      "name": "Astronomija Višnjan",
      "URL": "https://astro.hr/"
    },
    {
      "id": 1,
      "name": "AU Vidulini",
      "URL": "http://vidulini-astro.hr/"
    },
    {
      "id": 2,
      "name": "Cenosco Croatia",
      "URL": "https://cenosco.com/"
    },
    {
      "id": 3,
      "name": "CMGC d.o.o.",
      "URL": "https://www.cmg.digital/"
    },
    {
      "id": 4,
      "name": "Plus Hosting Grupa d.o.o.",
      "URL": "https://www.plus.hr"
    },
    {
      "id": 5,
      "name": "Express agencija d.o.o.",
      "URL": "http://www.regionalexpress.hr/site/more/impressum"
    },
    {
      "id": 6,
      "name": "FWD Grupa",
      "URL": "http://fwd.hr"
    },
    {
      "id": 7,
      "name": "Geogrupa d.o.o.",
      "URL": "https://geo-grupa.hr"
    },
    {
      "id": 8,
      "name": "IN2 d.o.o.",
      "URL": "https://in2.hr"
    },
    {
      "id": 9,
      "name": "Infobip d.o.o.",
      "URL": "https://infobip.com"
    },
    {
      "id": 10,
      "name": "Infosit d.o.o.",
      "URL": "https://www.infosit.com"
    },
    {
      "id": 11,
      "name": "Intersoft Technologies d.o.o.",
      "URL": "https://www.intersoft.uno"
    },
    {
      "id": 12,
      "name": "A&R Carton Istra",
      "URL": "https://www.ar-carton.com/en/"
    },
    {
      "id": 13,
      "name": "Infosit d.o.o.",
      "URL": "https://www.infosit.com"
    },
    {
      "id": 14,
      "name": "ISTRA TECH d.o.o.",
      "URL": "http://www.istratech.hr"
    },
    {
      "id": 15,
      "name": "Lloyds Design d.o.o.",
      "URL": "https://lloyds-design.com"
    },
    {
      "id": 16,
      "name": "Infosit d.o.o.",
      "URL": "https://www.infosit.com"
    },
    {
      "id": 17,
      "name": "Maistra d.d.",
      "URL": "https://maistra.hr"
    },
    {
      "id": 18,
      "name": "Mijena d.o.o.",
      "URL": "https://mijena.com"
    },
    {
      "id": 19,
      "name": "Neo Lab d.o.o.",
      "URL": "https://www.neolab.hr"
    },
    {
      "id": 20,
      "name": "Penta d.o.o.",
      "URL": "https://www.penta.hr"
    },
    {
      "id": 21,
      "name": "Pula Film Festival",
      "URL": "https://www.pulafilmfestival.hr"
    },
    {
      "id": 22,
      "name": "QiQo d.o.o.",
      "URL": "http://qiqo.hr"
    },
    {
      "id": 23,
      "name": "Spectral Core d.o.o.",
      "URL": "https://www.spectralcore.com"
    },
    {
      "id": 24,
      "name": "Superius d.o.o.",
      "URL": "https://superius.co"
    },
    {
      "id": 25,
      "name": "Superius Idea d.o.o.",
      "URL": "http://superiusidea.hr"
    },
    {
      "id": 26,
      "name": "Sysbee d.o.o.",
      "URL": "https://www.sysbee.net"
    },
    {
      "id": 27,
      "name": "Red Martyr Entertainment",
      "URL": "http://www.tanaisgames.com"
    },
    {
      "id": 28,
      "name": "Uniline d.o.o.",
      "URL": "https://www.uniline.hr/croatia/"
    },
    {
      "id": 29,
      "name": "Valamar d.d.",
      "URL": "https://www.valamar.com"
    },
    {
      "id": 30,
      "name": "TRI M d.o.o.",
      "URL": "https://tri-m.hr"
    },
    {
      "id": 31,
      "name": "NK Istra 1961 š.d.d.",
      "URL": "https://nkistra.com"
    },
    {
      "id": 32,
      "name": "H.3 Solutions d.o.o.",
      "URL": "https://www.h3.solutions/"
    },
    {
      "id": 33,
      "name": "E.Studio d.o.o.",
      "URL": "https://www.estudio.hr/"
    },
    {
      "id": 34,
      "name": "AB-PROJEKT d.o.o.",
      "URL": ""
    },
    {
      "id": 35,
      "name": "Fury Studios d.o.o.",
      "URL": "https://rawfury.com/"
    },
    {
      "id": 36,
      "name": "LINK LAB j.d.o.o.",
      "URL": "http://www.linklab.hr/"
    },
    {
      "id": 37,
      "name": "UTE d.o.o.",
      "URL": ""
    },
    {
      "id": 38,
      "name": "Tri plus grupa d.o.o.",
      "URL": ""
    },
    {
      "id": 39,
      "name": "PLAY DIGITAL d.o.o.",
      "URL": "https://www.playdigital.hr/"
    },
    {
      "id": 40,
      "name": "Institut Ruđer Bošković",
      "URL": "irb.hr"
    },
    {
      "id": 41,
      "name": "DAH Istra d.o.o.",
      "URL": ""
    }
    ]
    return jobs

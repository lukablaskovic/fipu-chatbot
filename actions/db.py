import pandas as pd


class fipuAPI(object):
    def __init__(self):
        self.db = pd.read_json("json/praksa_poduzeca_zadaci.json")

    def fetch_data(self):
        return self.db["companies"]

    def epic(self):
        return self.db["companies"]


def get_internship_details(id, name):
    db = pd.read_json("json/praksa_poduzeca_zadaci.json")

    data_list = db["companies"]

    for item in data_list:
        if item["id"] == id or item["name"] == name:
            print(f"get_internship_details: Found {item['name']} !")
            return item
    return None


def get_available_companies():
    db = pd.read_json("json/praksa_poduzeca_zadaci.json")
    # Return available companies names in array, list comprehension
    data_list = db["companies"]
    return [item["name"] for item in data_list]

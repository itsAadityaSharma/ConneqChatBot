# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
import authJWTs as authJWTs
from rasa_sdk.executor import CollectingDispatcher
import requests


from datetime import datetime
from tabulate import tabulate


# response = requests.get(url)
# if response.status_code == 200:
#     data = response.json()
    # Process the data here
    # print(data)


def remove_fields(obj, fields_to_remove):
    if not isinstance(obj, dict):
        return obj
    result = {}
    for key, value in obj.items():
        if key not in fields_to_remove:
            if isinstance(value, dict):
                result[key] = remove_fields(value, fields_to_remove)
            elif isinstance(value, list):
                result[key] = [remove_fields(item, fields_to_remove) for item in value]
            else:
                result[key] = value
    return result


class ActionGetLeaves(Action):

    def name(self) -> Text:
        return "action_get_leaves"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        url = 'https://ge39e7b01ee1b6f-connetqdevdb.adb.ap-mumbai-1.oraclecloudapps.com/ords/test_schema/conneqtion_leave/?q={"emp_id":1}'

        try:
            response = requests.get(url=url)
            response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
            data = response.json()
            items = data['items'][0]
            annual_leave = items.get('annual_leave')
            casual_leave = items.get('casual_leave')
            # annual_leave_Entity=next(tracker.get_latest_entity_values("holidayType"),None)
            leave_Entity=tracker.latest_message.get('entities',[])
            # print(leave_Entity[0].get('value').upper()=="ANNUAL LEAVES")
            if(len(leave_Entity)>1):
                dispatcher.utter_message(text=f'You have annual leave {annual_leave} and casual leave {casual_leave}')
            elif(leave_Entity[0].get('value').upper()=="ANNUAL LEAVES"):
                dispatcher.utter_message(text=f'You have annual leave {annual_leave} only')
            elif(leave_Entity[0].get('value').upper()=="CASUAL LEAVES"):
                dispatcher.utter_message(text=f'You have casual leave {casual_leave} only')
            elif(leave_Entity[0].get('value').upper()=="TOTAL LEAVES"):
                dispatcher.utter_message(text=f'You TOTAL have annual leave {annual_leave} and casual leave {casual_leave}')
            elif(len(leave_Entity)<1):
                dispatcher.utter_message(text='Which leaves type do you want?')

        except requests.exceptions.RequestException as e:
            print("Error fetching data:", e)
            dispatcher.utter_message(text="Failed to fetch leave data. Please try again later.")
        
        except (KeyError, IndexError) as e:
            print("Error parsing response:", e)
            dispatcher.utter_message(text="Error parsing leave data. Please try again later.")
        
        return []
    
    # ----------new --------------# 

class ActionGetUpcomingHolidays(Action):

    def name(self) -> Text:
        return "upcomingHolidays"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        url = 'https://ge39e7b01ee1b6f-connetqdevdb.adb.ap-mumbai-1.oraclecloudapps.com/ords/test_schema/holiday_calendar/'
        
        try:

            response = requests.get(url=url)
            response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
            data = response.json()
            items = data['items']
            headers = "keys"  # Use "keys" to automatically use dictionary keys as headers
            
            # dispatcher.utter_message(text=f'Upcoming Leaves are {items}')
            current_date = datetime.now().date()
            print(current_date)
            result = [
    {key: value for key, value in item.items() if key != 'links'}
    for item in items
    if datetime.strptime(item["holiday_date"], "%Y-%m-%dT%H:%M:%SZ").date() > current_date
]
            print(result)

            if(tracker.get_latest_entity_values=="holidayType"):
                pass
            elif (tracker.get_latest_entity_values=="holidayType"):
                pass
            table = tabulate(result, headers=headers, tablefmt="grid")
            dispatcher.utter_message(text=f"Here is the data:\n{table}")
            # dispatcher.utter_message(json_message)
#             current_date = datetime.date.today()
        
        except requests.exceptions.RequestException as e:
            print("Error fetching data:", e)
            dispatcher.utter_message(text="Failed to fetch leave data. Please try again later.")
        
        except (KeyError, IndexError) as e:
            print("Error parsing response:", e)
            dispatcher.utter_message(text="Error parsing leave data. Please try again later.")
        
        return []



class ActionGetEmpData(Action):

    def name(self) -> Text:
        return "action_get_EmpData"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        url = 'https://ge39e7b01ee1b6f-connetqdevdb.adb.ap-mumbai-1.oraclecloudapps.com/ords/test_schema/employees_data?q={"first_name":{"$instr":"'
        
        try:
            nameEntity=tracker.latest_message.get('entities',[])
            print(nameEntity)
            url=url+f'{nameEntity[0].get("value")}"'+"}"+"}"
            print(url)
            response = requests.get(url=url)
            response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
            data = response.json()
            # items = data['items']
            headers = "keys"
            # annual_leave = items.get('annual_leave')
            # casual_leave = items.get('casual_leave')
            items = remove_fields(data,["links","count","offset","hasMore","limit","updated_on","updated_by","created_on","created_by"])
            # print(items)
            table = tabulate(items['items'], headers=headers, tablefmt="grid")
            dispatcher.utter_message(text=f'Employee Data : {table}')
            
        
        except requests.exceptions.RequestException as e:
            print("Error fetching data:", e)
            dispatcher.utter_message(text="Failed to fetch leave data. Please try again later.")
        
        except (KeyError, IndexError) as e:
            print("Error parsing response:", e)
            dispatcher.utter_message(text="Error parsing leave data. Please try again later.")
        
        return []
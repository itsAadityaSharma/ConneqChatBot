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

class ActionGetLeaves(Action):

    def name(self) -> Text:
        return "action_get_leaves"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("hello world")
        print(tracker.sender_id)
        
        url = 'https://ge39e7b01ee1b6f-connetqdevdb.adb.ap-mumbai-1.oraclecloudapps.com/ords/test_schema/conneqtion_leave/?q={"emp_id":1}'
        
        try:
            response = requests.get(url=url)
            response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
            data = response.json()
            items = data['items'][0]
            annual_leave = items.get('annual_leave')
            casual_leave = items.get('casual_leave')
            dispatcher.utter_message(text=f'You have annual leave {annual_leave} and casual leave {casual_leave}')
            
        
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
#             current_date = datetime.date.today()

# # Print current date
#             print("Current date:", current_date)






        
        except requests.exceptions.RequestException as e:
            print("Error fetching data:", e)
            dispatcher.utter_message(text="Failed to fetch leave data. Please try again later.")
        
        except (KeyError, IndexError) as e:
            print("Error parsing response:", e)
            dispatcher.utter_message(text="Error parsing leave data. Please try again later.")
        
        return []


# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

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
        
        url = 'https://ge39e7b01ee1b6f-connetqdevdb.adb.ap-mumbai-1.oraclecloudapps.com/ords/test_schema/employeeleaves/'
        leaveType=tracker.latest_message['entities'][0]['value']
        print(leaveType)
        dispatcher.utter_message(text="This is get Leaves")
        return []

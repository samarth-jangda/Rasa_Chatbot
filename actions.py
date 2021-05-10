from typing import Any , Text , Dict , List

from rasa_sdk import Action , Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class ActioHelloWorld(Action):

    def name(self) -> Text:
        return "General_Form"

    @staticmethod
    def required_slots(tracker: Tracker)-> List[Text]:
        """A list of required slots that the form has to fill """
        print("required_slots(tracker: Tracker)")
        return["name","email","phonenumber"]



    def submit(self , dispatcher: CollectingDispatcher ,
            tracker: Tracker,
            domain: Dict[Text,Any])-> List[Dict]:
        dispatcher.utter_message(template="utter_submit")

        return[]
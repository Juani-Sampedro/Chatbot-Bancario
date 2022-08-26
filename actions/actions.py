# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionTarjetaDeCredito(Action):

     def name(self) -> Text:
        return "action_tarjeta_de_credito"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        intent = (tracker.latest_message)['text']
        dispatcher.utter_message(text="Perfecto, a continuación te diré qué tienes que hacer")
        if ((str(intent)=="si") or (str(intent)=="si obvio")):
            dispatcher.utter_message(text="Entrá a tu Online Banking y en Tarjetas elegí la opción de Solicitar tarjeta.")
        elif ((str(intent)=="no") or (str(intent)=="no lo soy") or (str(intent)=="no aun")): 
            dispatcher.utter_message(text="Ingresá a nuestra pagina web y formá parte de nuestra comunidad")
            
        return []

class ActionCajadeAhorro(Action):

     def name(self) -> Text:
        return "action_caja_de_ahorro"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        intent = (tracker.latest_message)['text']
        dispatcher.utter_message(text="Perfecto, a continuación te diré qué tienes que hacer")
        if ((str(intent)=="si") or (str(intent)=="si obvio")):
            dispatcher.utter_message(text="Entrás a la parte de Cuentas en tu Online Banking y elegís la opción que dice Nueva Caja de ahorro.")
        elif ((str(intent)=="no") or (str(intent)=="no lo soy") or (str(intent)=="no aun")): 
            dispatcher.utter_message(text="Ingresá a nuestra pagina web y formá parte de nuestra comunidad")
            
        return []

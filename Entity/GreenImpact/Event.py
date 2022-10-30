from datetime import datetime


class Event:
    def __init__(self, event: dict):
        self.id = event["id"]
        self.title = event["title"]
        self.description = event["description"]
        self.start_at = event["startAt"]
        self.end_at = event["endAt"]
        self.status = "Créer" if str(event["status"][0]) == "0" else "En cours" if str(event["status"][0]) == "1" else "Terminé"

    def to_dict_trello(self) -> dict:
        """
        Return dict for trello

        Returns:
            dict
        """
        return {
            "name": f"{self.id};{self.title}",
            "desc": self.description,
        }

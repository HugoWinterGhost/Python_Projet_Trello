from Provider import Trello, GreenImpact
from Controller import GreenImpactEventController


class AutoController:

    @staticmethod
    def update_card(trello: Trello, event_controller: GreenImpactEventController, green_impact: GreenImpact) -> None:
        """
        Update a card if an update have been made

        Args:
            trello:
            event_controller:
            green_impact:

        Returns:
            None
        """
        for event in event_controller.events:
            if card := [card for card in trello.cards if f"{event.id};" in card.name and (event.title not in card.name or event.description != card.desc)]:
                event_json = {
                    "title": card[0].name.split(";")[1],
                    "description": card[0].desc
                }
                green_impact.update("events", event.id, event_json)

    @staticmethod
    def move_card(trello: Trello, event_controller: GreenImpactEventController) -> None:
        """
        Move card if the status have been updated

        Args:
            trello:
            event_controller:

        Returns:
            None
        """
        for event in event_controller.events:
            card = [card for card in trello.cards if card.name == f"{event.id};{event.title}"]
            if not card:
                continue
            list_id = [a_list.id for a_list in trello.lists if a_list.name == event.status]
            if not card[0] in trello.board[list_id[0]]["cards"]:
                trello.edit_card(card[0].id, {"idList": list_id[0]})

    @staticmethod
    def create_card(trello: Trello, event_controller: GreenImpactEventController) -> None:
        """
        Create a card if an entity have been created

        Args:
            trello:
            event_controller:

        Returns:
            None
        """
        for event in event_controller.events:
            if not [card for card in trello.cards if card.name == f"{event.id};{event.title}"]:
                card_json = event.to_dict_trello()

                if not (list_id := [a_list.id for a_list in trello.lists if a_list.name == event.status]):
                    if trello_list := trello.create_list({"name": event.status, "idBoard": trello.board_id}):

                        card_json["idList"] = trello_list.id
                else:
                    card_json["idList"] = list_id[0]

                trello.create_card(card_json)

    @staticmethod
    def delete_card(trello: Trello, event_controller: GreenImpactEventController) -> None:
        """
        Delete all card who is not related to the other api

        Args:
            trello:
            event_controller:

        Returns:
            None
        """
        for card in trello.cards:
            if not [event for event in event_controller.events if card.name == f"{event.id};{event.title}"]:
                trello.delete_card(card.id)

    @staticmethod
    def delete_event(trello: Trello, green_impact: GreenImpactEventController) -> None:
        """
        Delete Card and entity if they have been moved in "A supprimer"

        Args:
            trello:
            green_impact:

        Returns:
            None
        """
        to_delete_list = [a_list for a_list in trello.lists if a_list.name == "A supprimer"]
        for card in trello.board[to_delete_list[0].id]["cards"]:
            event_id = card.name.split(";")[0]
            trello.delete_card(card.id)
            green_impact.delete("events", event_id)

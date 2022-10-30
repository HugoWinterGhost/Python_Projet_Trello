from Provider import GreenImpact, Trello
from Controller import GreenImpactEventController, AutoController


def auto() -> None:
    """
    Make all the update

    Returns:
        None
    """
    green_impact = GreenImpact()
    trello = Trello()

    # met à jour
    trello.set_up()
    event_controller = GreenImpactEventController(green_impact.get_all("events"))
    AutoController.update_card(trello, event_controller, green_impact)

    # delete un event
    trello.set_up()
    AutoController.delete_event(trello, green_impact)

    # déplace
    trello.set_up()
    event_controller = GreenImpactEventController(green_impact.get_all("events"))
    AutoController.move_card(trello, event_controller)

    # créer une carte event
    trello.set_up()
    event_controller = GreenImpactEventController(green_impact.get_all("events"))
    AutoController.create_card(trello, event_controller)

    # supprime une carte
    trello.set_up()
    event_controller = GreenImpactEventController(green_impact.get_all("events"))
    AutoController.delete_card(trello, event_controller)


if __name__ == "__main__":
    auto()

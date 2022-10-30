class TrelloCardsController:
    def __init__(self, trello_cards: list):
        self.cards = trello_cards

    def list_all_card(self) -> None:
        """
        List all card

        Returns:
            None
        """
        for i, card in enumerate(self.cards, 1):
            print(f"{i}. {card.name}")

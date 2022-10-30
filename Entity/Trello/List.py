class List:
    def __init__(self, trello_list: dict, cards: list = None):
        self.id = trello_list["id"]
        self.name = trello_list["name"]
        self.cards = cards

    def to_string(self) -> None:
        """
        To string

        Returns:
            None
        """
        print(f"""
id: {self.id}
nom: {self.name}
""")

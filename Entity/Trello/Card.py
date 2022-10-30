class Card:
    def __init__(self, trello_card: dict):
        self.id = trello_card["id"]
        self.name = trello_card["name"]
        self.desc = trello_card["desc"]
        self.due = trello_card["due"]
        self.id_list = trello_card["idList"]

    def to_string(self) -> None:
        """
        To string

        Returns:
            None
        """
        print(f"""
id: {self.id}
nom: {self.name}
description: {self.desc}
due: {self.due}
""")

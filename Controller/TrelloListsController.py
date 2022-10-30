class TrelloListsController:
    def __init__(self, trello_lists: list):
        self.lists = trello_lists

    def list_all_trello_list(self) -> None:
        """
        list all trello list

        Returns:
            None
        """
        for i, a_list in enumerate(self.lists, 1):
            print(f"{i}. {a_list.name}")

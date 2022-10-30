from time import sleep, perf_counter

from dotenv import dotenv_values
from requests import post, get, put, delete

from Entity import Card
from Entity import List
from .Discord import Discord


class Trello:

    def __init__(self) -> None:
        self.params = {
            "key": dotenv_values(".env")["KEY"],
            "token": dotenv_values(".env")["TOKEN"]
        }
        self.host = "https://api.trello.com/1/"
        self.index = 0
        self.start = perf_counter()
        self.board_id = "62277e6b2bd5097482cab065"
        self.board = {}

        self.cards = []
        self.lists = []

    def set_up(self):

        self.cards = self.get_all_cards()
        self.lists = self.get_all_list()
        self.get_board()

    def get_all_cards(self, filter: dict = None) -> list:
        """
        Get all cards

        Args:
            filter : trello api filter

        Returns:
            list
        """
        if filter is None:
            filter = {}

        res = get(
            self.host + "boards/" + self.board_id + "/cards",
            params=self.params,
            json=filter
        )
        self.pause()

        if res.status_code == 200:
            return self.__format_cards(res.json())
        Discord().post_error(f"get_all_cards({filter})", res.text)
        print("Erreur", res.text)
        return []

    def get_all_list(self, filter: dict = None) -> list:
        """
        Get all list

        Args:
            filter : trello api filter

        Returns:
            list
        """
        if filter is None:
            filter = {}

        res = get(
            self.host + "boards/" + self.board_id + "/lists",
            params=self.params,
            json=filter
        )
        self.pause()

        if res.status_code == 200:
            return self.__format_lists(res.json())
        Discord().post_error(f"get_all_list({filter})", res.text)
        print("Erreur", res.text)
        return []

    def get_board(self) -> None:
        """
        Format to become the board

        Returns:
            None
        """
        for a_list in self.lists:
            self.board[a_list.id] = {
                "name": a_list.name,
                "cards": [card for card in self.cards if card.id_list == a_list.id]
            }

    def get_all_cards_list(self, list_id: (str, int), filter: dict = None) -> list:
        """
        Get all cards

        Args:
            list_id: list id
            filter : trello api filter

        Returns:
            list
        """
        if filter is None:
            filter = {}

        res = get(
            self.host + "lists/" + list_id + "/cards",
            params=self.params,
            json=filter
        )
        self.pause()

        if res.status_code == 200:
            return self.__format_lists(res.json())
        Discord().post_error(f"get_all_cards_list({list_id}, {filter})", res.text)
        print("Erreur", res.text)
        return []

    def get_one_card(self, card_id: (str, int), card_json: dict = None) -> (None, Card):
        """
        get one card

        Args:
            card_id: card id
            card_json: filter

        Returns:
            (None, Card)
        """
        if card_json is None:
            card_json = {}

        res = get(
            self.host + "cards/" + card_id,
            params=self.params,
            json=card_json
        )
        self.pause()

        if res.status_code == 200:
            return Card(res.json())
        Discord().post_error(f"get_one_card({card_id}, {card_json})", res.text)
        print(res.text)
        return

    def create_card(self, card_json: dict) -> (None, Card):
        """
        Create a Card in trello

        Args:
            card_json: card information

        Returns:
            (None, Card)
        """
        res = post(
            self.host + "cards",
            params=self.params,
            json=card_json,
        )
        self.pause()

        if res.status_code == 200:
            self.cards.append(Card(res.json()))
            return Card(res.json())
        Discord().post_error(f"create_card({card_json})", res.text)
        print(res.text)
        return
    
    def create_list(self, list_json: dict) -> (None, List):
        """
        Create a list in Trello

        Args:
            list_json: list information

        Returns:
            (None, List)
        """
        res = post(
            self.host + "lists",
            params=self.params,
            json=list_json,
        )
        self.pause()

        if res.status_code == 200:
            self.lists.append(List(res.json()))
            return List(res.json())
        Discord().post_error(f"create_list({list_json})", res.text)
        print(res.text)
        return

    def edit_card(self, card_id: (str, int), card_json: dict) -> (None, Card):
        """
        Permet d'éditer une carte

        Args:
            card_id: card id
            card_json: card information

        Returns:
            (None, Card)
        """

        res = put(
            self.host + "cards/" + card_id,
            params=self.params,
            json=card_json,
        )
        self.pause()

        if res.status_code == 200:
            return Card(res.json())
        Discord().post_error(f"edit_card({card_id}, {card_json}", res.text)
        print(res.text)
        return

    def edit_list(self, list_id: (str, int), list_json: dict) -> (None, List):
        """
        Permet d'éditer une liste

        Args:
            list_id: list id
            list_json: list information

        Returns:
            (None, List)
        """

        res = put(
            self.host + "lists/" + list_id,
            params=self.params,
            json=list_json,
        )
        self.pause()

        if res.status_code == 200:
            return List(res.json())
        Discord().post_error(f"edit_list({list_id}, {list_json})", res.text)
        print(res.text)
        return

    def delete_card(self, card_id: (str, int)) -> dict:
        """

        Args:
            card_id: card id

        Returns:
            dict
        """

        res = delete(
            self.host + "cards/" + card_id,
            params=self.params,
        )

        if res.status_code == 200:
            return res.json()
        Discord().post_error(f"delete_card({card_id})", res.text)
        print(res.text)
        return {}

    def delete_list(self, list_id: (str, int)) -> dict:
        """

        Args:
            list_id: list id

        Returns:
            dict
        """

        res = put(
            self.host + "lists/" + list_id + "/closed",
            params=self.params,
            json={"value":True}
        )

        if res.status_code == 200:
            return res.json()
        Discord().post_error(f"delete_list({list_id})", res.text)
        print(res.text)
        return {}

    def pause(self) -> None:
        """Put the script to sleep if 10 requests have been executed in less than 1 second.

        Returns:
            None
        """
        sleep(0.001)
        self.index += 1
        if self.index >= 10:
            self.index = 0
            finish = perf_counter()
            if int(finish - self.start) < 10:
                sleep(round(finish - self.start, 2))
                self.start = perf_counter()

    @staticmethod
    def __format_cards(trello_cards: list) -> list:
        """
        Format list of trello card

        Args:
            trello_cards:

        Returns:
            list
        """
        cards = []
        for card in trello_cards:
            if "id" not in card.keys() and "name" not in card.keys() and "desc" not in card.keys():
                Discord().post_error(f"__format_list(trello_cards)", card)
                print(f"Error : {card}")
                continue
            cards.append(Card(card))
        return cards

    @staticmethod
    def __format_lists(trello_lists: list) -> list:
        """
        Format list of trello list

        Args:
            trello_lists:

        Returns:
            list
        """
        lists = []
        for trello_list in trello_lists:
            if "id" not in trello_list.keys() and "name" not in trello_list.keys():
                Discord().post_error(f"__format_list(trello_list)", trello_list)
                print({trello_list})
                continue
            lists.append(List(trello_list))
        return lists

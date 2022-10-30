from Provider import Trello
from .TrelloListsController import TrelloListsController
from .TrelloCardsController import TrelloCardsController
from Entity import List, Card


class Choice:
    def __init__(self, cards=None, trello_lists=None):
        self.cards = cards if cards is not None else []
        self.lists = trello_lists if trello_lists is not None else []

    def choice_3(self) -> None:
        """
        Permet de lister toutes les cartes d'une liste

        Returns:
            None
        """
        TrelloListsController(self.lists).list_all_trello_list()
        a_list = self.__choose_list()
        
        cards = Trello().get_all_cards_list(a_list.id)
        print("Voici les cartes" if cards else "Il n'y a aucune carte dans votre liste")
        TrelloCardsController(cards).list_all_card()
    
    def choice_4(self) -> None:
        """
        Permet d'afficher une carte trello de son choix

        Returns:
            None
        """
        TrelloCardsController(self.cards).list_all_card()
        while True:
            try:
                num = int(input("Veuillez choisir la carte :\n"))
                break
            except ValueError:
                print("Veuillez saisir un nombre valide sans espace")

        card = [card for i, card in enumerate(self.cards) if i + 1 == num]

        if card:
            card[0].to_string()
        else:
            print("Aucune carte selectionnée")

    def choice_5(self) -> None:
        """
        Permet de créer une carte sur le tableau trello dans la liste choisie

        Returns:
            None
        """
        TrelloListsController(self.lists).list_all_trello_list()
        a_list = self.__choose_list()

        json_card = {
            "name": input("Veuillez saisir un nom pour votre carte: \n"),
            "desc": input("Veuillez saisir une description:\n"),
            "idList": a_list.id
        }
        print("""
----------------------------------------
        """)
        if card := Trello().create_card(json_card):
            print(f"Votre carte {card.name} a bien été créée !!")
            return
        print("Votre carte n'a pas été créée")

    def choice_6(self) -> None:
        """
        Permet de créer une liste sur le tableau trello dans le board choisi

        Returns:
            None
        """
        TrelloListsController(self.lists).list_all_trello_list()
        json_list = {
            "name": input("Veuillez saisir un nom pour votre liste: \n"),
            "idBoard": Trello().board_id
        }

        print("""
----------------------------------------
        """)
        if a_list := Trello().create_list(json_list):
            print(f"Votre liste {a_list.name} a bien été créée !!")
            return
        print("Votre liste n'a pas été créée")

    def choice_7(self) -> None:
        """
        Permet d'éditer une carte

        Returns:
            None
        """
        TrelloCardsController(self.cards).list_all_card()
        card = self.__choose_card()
        json_card = {}
        if name := input("Veuillez saisir le nouveau nom de la carte sinon ne saisissez rien\n"):
            json_card["name"] = name
        if desc := input("Veuillez saisir la nouvelle description de la carte sinon ne saisissez rien\n"):
            json_card["desc"] = desc
        print("""
----------------------------------------
        """)

        if json_card:
            if Trello().edit_card(card.id, json_card):
                print("Ta carte a bien été modifiée !!")
                return
            return
        print("Tu n'as rien saisi")

    def choice_8(self) -> None:
        """
        Permet d'éditer une liste

        Returns:
            None
        """
        TrelloListsController(self.lists).list_all_trello_list()
        a_list = self.__choose_list()
        json_list = {}
        if name := input("Veuillez saisir le nouveau nom de la liste sinon ne saisissez rien\n"):
            json_list["name"] = name
        print("""
----------------------------------------
        """)

        if json_list:
            if Trello().edit_list(a_list.id, json_list):
                print("Ta liste a bien été modifiée !!")
                return
            return
        print("Tu n'as rien saisi")

    def choice_9(self) -> None:
        """
        Permet de déplacer une carte

        Returns:
            None
        """
        TrelloCardsController(self.cards).list_all_card()
        card = self.__choose_card()
        print("==========================================")
        TrelloListsController(self.lists).list_all_trello_list()
        trello_list = self.__choose_list()
        print("""
----------------------------------------
        """)

        if card := Trello().edit_card(card.id, {"idList": trello_list.id}):
            print(f"La carte {card.name} a bien été déplacée dans la liste {trello_list.name}")
            return
        print(f"La carte {card.name} n'a pas été déplacée dans la liste {trello_list.name} ")

    def choice_10(self) -> None:
        """
        Permet de supprimer une carte

        Returns:
            None
        """
        TrelloCardsController(self.cards).list_all_card()
        card = self.__choose_card()
        print("""
----------------------------------------
        """)

        if Trello().delete_card(card.id):
            print("La carte a bien été supprimée !!")
            return
        print("La carte n'a pas été supprimée")

    def choice_11(self) -> None:
        """
        Permet de supprimer une liste

        Returns:
            None
        """
        TrelloListsController(self.lists).list_all_trello_list()
        a_list = self.__choose_list()
        print("""
----------------------------------------
        """)

        if Trello().delete_list(a_list.id):
            print("La liste a bien été supprimée !!")
            return
        print("La list n'a pas été supprimée")

    def __choose_card(self) -> Card:
        """
        Permet de selectionner une carte

        Returns:
            Card
        """
        while True:
            try:
                num = int(input("Veuillez choisir la carte :\n"))
                card = [card for i, card in enumerate(self.cards) if i + 1 == num]
                if card:
                    return card[0]
                print("La liste choisie n'existe pas")
            except ValueError:
                print("Veuillez saisir un nombre valide sans espace")

    def __choose_list(self) -> List:
        """
        Permet de choisir la liste

        Returns:
            List
        """
        while True:
            try:
                num = int(input("Veuillez saisir le numéro de la liste :\n"))
                a_list = [trello_list for i, trello_list in enumerate(self.lists) if i + 1 == num]
                if a_list:
                    return a_list[0]
                print("La liste choisie n'existe pas")
            except ValueError:
                print("\n /!\\ Veuillez saisir un nombre valide sans espace /!\\ \n")

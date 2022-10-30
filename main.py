import sys

from Provider import Trello
from Controller import TrelloCardsController, TrelloListsController, Choice


def main() -> None:
    """
    Main function of the cmd application

    Returns:
        None
    """
    print("""
████████╗██████╗ ███████╗██╗     ██╗      ██████╗ 
╚══██╔══╝██╔══██╗██╔════╝██║     ██║     ██╔═══██╗
   ██║   ██████╔╝█████╗  ██║     ██║     ██║   ██║
   ██║   ██╔══██╗██╔══╝  ██║     ██║     ██║   ██║
   ██║   ██║  ██║███████╗███████╗███████╗╚██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝ 
                                               
        """)
    
    MENU = """Choisissez parmi les options suivantes :
    1: Afficher vos listes
    2: Afficher toutes les cartes
    3: Afficher les cartes d'une liste
    4: Afficher une carte
    5: Créer une carte
    6: Créer une liste
    7: Éditer une carte
    8: Éditer une liste
    9: Déplacer une carte
    10: Supprimer une carte
    11: Supprimer une liste
    12: Quitter l'application

Votre choix : """

    OPTIONS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

    while True:

        trello = Trello()
        trello.set_up()

        user_choice = ""
        while user_choice not in OPTIONS:
            user_choice = input(MENU)
            print("""
----------------------------------------
        """)
            if user_choice not in OPTIONS:
                print("""
----------------------------------------
                """)
                print("Choisissez un chiffre correspondant aux options disponibles")

        if user_choice == "1":
            print("Voici les listes" if trello.lists else "Il n'y a aucune liste sur votre tableau")
            TrelloListsController(trello.lists).list_all_trello_list()

        elif user_choice == "2":
            print("Voici les cartes" if trello.cards else "Il n'y a aucune cartes sur votre tableau")
            TrelloCardsController(trello.cards).list_all_card()

        elif user_choice == "3":
            Choice(trello_lists=trello.lists).choice_3()

        elif user_choice == "4":
            Choice(cards=trello.cards).choice_4()

        elif user_choice == "5":
            Choice(trello_lists=trello.lists).choice_5()

        elif user_choice == "6":
            Choice(trello_lists=trello.lists).choice_6()

        elif user_choice == "7":
            Choice(cards=trello.cards).choice_7()

        elif user_choice == "8":
            Choice(trello_lists=trello.lists).choice_8()

        elif user_choice == "9":
            Choice(cards=trello.cards, trello_lists=trello.lists).choice_9()

        elif user_choice == "10":
            Choice(cards=trello.cards).choice_10()

        elif user_choice == "11":
            Choice(trello_lists=trello.lists).choice_11()

        elif user_choice == "12":
            print("""
 ██████╗  ██████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███████╗
██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝
██║  ███╗██║   ██║██║   ██║██║  ██║██████╔╝ ╚████╔╝ █████╗  
██║   ██║██║   ██║██║   ██║██║  ██║██╔══██╗  ╚██╔╝  ██╔══╝  
╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝██████╔╝   ██║   ███████╗
 ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝
                                                            
            """)
            sys.exit()
        print("""
----------------------------------------
        """)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("""
 ██████╗  ██████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███████╗
██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝
██║  ███╗██║   ██║██║   ██║██║  ██║██████╔╝ ╚████╔╝ █████╗  
██║   ██║██║   ██║██║   ██║██║  ██║██╔══██╗  ╚██╔╝  ██╔══╝  
╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝██████╔╝   ██║   ███████╗
 ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝
                                                            
            """)
        sys.exit()

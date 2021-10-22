class Player:
    def __init__(self):
        self.cards = []

    def append(self, n):
        self.cards.append(n)

    # what the player does

    # def player_actions(self, player_sum, player_cards):
    #     bust = 0
    #     blackjack = 1
    #     stay = 2
    #     bust_twice = 3
    #     split_stay = 4  # both hands stay or if the 1st hand busts
    #     player_cards_2 = [0, 0]  # in case there's no split

    #     if player_sum != 21:

    #         response = ''
    #         # when both cards are the same, the option for split comes up
    #         if player_cards[0] == player_cards[1]:

    #             while response != "stay":
    #                 response = str(input(
    #                     "Would you like to hit, stay, or split? Type 'hit', type 'stay', or type 'split'.\n"))

    #                 if response == "hit":
    #                     player_cards, og_cards, player_sum = hit(
    #                         ace(player_cards))
    #                     print(f'My cards: {og_cards} = {player_sum}\n')
    #                     if player_sum > 21:
    #                         player_sum = convert(player_cards)
    #                         return bust, player_cards_2
    #                     elif player_sum == 21:
    #                         return stay, player_cards_2

    #                 elif response == "stay":
    #                     player_sum = convert(player_cards)
    #                     return stay, player_cards_2

    #                 elif response == 'split':
    #                     s_response, player_cards_2 = split(player_cards)
    #                     if s_response == 0:
    #                         return stay, player_cards_2
    #                     elif s_response == 1:
    #                         return split_stay, player_cards_2
    #                     elif s_response == 2:
    #                         return bust_twice, player_cards_2

    #         elif player_cards[0] != player_cards[1]:
    #             while response != "stay":
    #                 response = str(
    #                     input("Would you like to hit or stay? Type 'hit' or type 'stay'.\n"))

    #                 if response == "hit":
    #                     player_cards, og_cards, player_sum = hit(player_cards)
    #                     print(f'My cards: {og_cards} = {player_sum}\n')
    #                     if player_sum > 21:
    #                         player_sum = convert(player_cards)
    #                         return bust, player_cards_2
    #                     elif player_sum == 21:
    #                         return stay, player_cards_2

    #                 elif response == "stay":
    #                     player_sum = convert(player_cards)
    #                     return stay, player_cards_2

    #     elif player_sum == 21 and len(player_cards) == 2:
    #         return blackjack, player_cards_2

    # # split cards for player

    # def split(self, cards):
    #     bust = 0
    #     stay = 1
    #     bust_twice = 2

    #     cards_2 = cards.copy()
    #     cards.pop()
    #     cards_2.pop()
    #     print(f'My 1st set of cards: {cards}')
    #     print(f'My 2nd set of cards: {cards_2}\n')

    #     response = ""
    #     response_2 = ""
    #     while response != "stay":
    #         response = str(input(
    #             "Would you like to hit or stay for your 1st hand? Type 'hit' or type 'stay'.\n"))

    #         if response == "hit":
    #             cards = dealing_cards(cards, 1)
    #             card_sum = convert(cards)
    #             print(f'My 1st set of cards: {cards} = {card_sum}')
    #             if card_sum > 21:
    #                 card_sum = convert(cards)
    #                 print('Your 1st hand busted...\n')

    #                 while response_2 != "stay":  # 2nd set of cards
    #                     response_2 = str(input(
    #                         "Would you like to hit or stay for your 2nd hand? Type 'hit' or type 'stay'.\n"))

    #                     if response_2 == "hit":
    #                         cards_2 = dealing_cards(cards_2, 1)
    #                         card_sum_2 = convert(cards_2)
    #                         print(
    #                             f'My 2nd set of cards: {cards_2} = {card_sum_2}\n')
    #                         if card_sum_2 > 21:
    #                             card_sum_2 = convert(cards_2)
    #                             return bust_twice
    #                         elif card_sum_2 == 21:
    #                             return stay, cards_2

    #                     elif response_2 == "stay":
    #                         card_sum_2 = convert(cards_2)
    #                         return stay, cards_2

    #         elif response == "stay":
    #             card_sum = convert(cards)

    #             while response_2 != "stay":  # 2nd set of cards
    #                 response_2 = str(input(
    #                     "Would you like to hit or stay for your 2nd hand? Type 'hit' or type 'stay'.\n"))

    #                 if response_2 == "hit":
    #                     cards_2 = dealing_cards(cards_2, 1)
    #                     card_sum_2 = convert(cards_2)
    #                     print(f'My 2nd set of cards: {cards_2} = {card_sum_2}')
    #                     if card_sum_2 > 21:
    #                         print('Your 2nd hand busted...\n')
    #                         return bust, cards_2
    #                     elif card_sum_2 == 21:
    #                         return stay, cards_2

    #                 elif response_2 == "stay":
    #                     card_sum_2 = convert(cards_2)
    #                     return stay, cards_2

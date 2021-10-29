from cards import Cards


class Player:
    def __init__(self):
        self.cards = []
        self.sum = 0
        # in case player splits
        self.cards2 = [0, 0]
        self.sum2 = 0

    # # what the player does

    def actions(self, c: Cards):
        if self.sum != 21:

            response = ''
            # when both cards are the same, the option for split comes up
            if self.cards[0] == self.cards[1]:

                while response != "stay":
                    response = str(input(
                        "Would you like to hit, stay, or split? Type 'hit', type 'stay', or type 'split'.\n"))

                    if response == "hit":
                        c.dealing_cards(self.cards, 1)
                        self.sum = c.convert(self.cards)
                        visible = self.cards.copy()
                        visible = c.ace(visible)
                        print(f'My cards: {visible} = {self.sum}\n')

                        if self.sum > 21:
                            return "bust"
                        elif self.sum == 21:
                            return "stay"

                    elif response == "stay":
                        self.sum = c.convert(self.cards)
                        return "stay"

                    # elif response == 'split':
                    #     s_response, player_cards_2 = split(player_cards)
                    #     if s_response == 0:
                    #         return stay, player_cards_2
                    #     elif s_response == 1:
                    #         return split_stay, player_cards_2
                    #     elif s_response == 2:
                    #         return bust_twice, player_cards_2

            elif self.cards[0] != self.cards[1]:
                while response != "stay":
                    response = str(
                        input("Would you like to hit or stay? Type 'hit' or type 'stay'.\n"))

                    if response == "hit":
                        c.dealing_cards(self.cards, 1)
                        self.sum = c.convert(self.cards)
                        visible = self.cards.copy()
                        visible = c.ace(visible)
                        print(f'My cards: {visible} = {self.sum}\n')

                        if self.sum > 21:
                            return "bust"
                        elif self.sum == 21:
                            return "stay"

                    elif response == "stay":
                        self.sum = c.convert(self.cards)
                        return "stay"

        elif self.sum == 21 and len(self.sum) == 2:
            return "blackjack"

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

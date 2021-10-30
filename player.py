class Player:
    def __init__(self):
        self.cards = []
        self.sum = 0
        # in case player splits
        self.cards2 = [0]
        self.sum2 = 0
        self.split_count = 0

    # # what the player does

    def actions(self, c):
        if self.sum == 21 and len(self.cards) == 2:
            return "blackjack"

        elif self.sum != 21:
            response = ''
            # when both cards are the same, the option for split comes up
            if self.cards[0] == self.cards[1] and self.split_count != 1:
                while response != "stay" and len(self.cards) == 2:
                    response = str(input(
                        "Would you like to hit, stay, or split? Type 'hit', 'stay', or 'split'.\n"))

                    if response == "hit":
                        c.dealing_cards(self.cards, 1)
                        self.sum = c.convert(self.cards)
                        visible = self.cards.copy()
                        visible = c.ace(visible)
                        print(f'My cards: {visible} = {self.sum}')

                        if self.sum > 21:
                            # if hand busts, sum is set to 0
                            self.sum = 0
                            response = "stay"
                        elif self.sum == 21:
                            response = "stay"

                    elif response == 'split':
                        self.cards2.clear()
                        self.split(c)
                        response = "stay"

            while response != "stay" and len(self.cards) >= 2:
                response = str(input(
                    "Would you like to hit or stay? Type 'hit' or 'stay'.\n"))

                if response == "hit":
                    c.dealing_cards(self.cards, 1)
                    self.sum = c.convert(self.cards)
                    visible = self.cards.copy()
                    visible = c.ace(visible)
                    print(f'My cards: {visible} = {self.sum}')

                    if self.sum > 21:
                        self.sum = 0
                        response = "stay"
                    elif self.sum == 21:
                        response = "stay"

    # split cards for player
    def split(self, c):
        self.split_count += 1
        self.cards2.append(self.cards.pop())
        print(f'My 1st set of cards: {self.cards}')
        print(f'My 2nd set of cards: {self.cards2}\n')

        response = ""
        while response != "stay":
            response = str(input(
                "Would you like to hit or stay for your 1st hand? Type 'hit' or 'stay'.\n"))

            if response == "hit":
                c.dealing_cards(self.cards, 1)
                self.sum = c.convert(self.cards)
                print(f'My 1st set of cards: {self.cards} = {self.sum}')
                if self.sum == 21 and len(self.cards) == 2:
                    self.hand_2nd(c)
                    response = "stay"

                elif self.sum > 21:
                    print('Your 1st hand busted...\n')
                    self.sum = 0
                    self.hand_2nd(c)
                    response = "stay"

            elif response == "stay":
                self.sum = c.convert(self.cards)
                self.hand_2nd(c)
                response = "stay"

    # computes the 2nd hand
    def hand_2nd(self, c):
        response_2 = ""
        while response_2 != "stay":  # 2nd set of cards
            response_2 = str(input(
                "Would you like to hit or stay for your 2nd hand? Type 'hit' or 'stay'.\n"))

            if response_2 == "hit":
                c.dealing_cards(self.cards2, 1)
                self.sum2 = c.convert(self.cards2)
                print(f'My 2nd set of cards: {self.cards2} = {self.sum2}\n')
                if self.sum2 > 21:
                    self.sum = 0
                    response_2 = "stay"
                elif self.sum2 == 21:
                    response_2 = "stay"

            elif response_2 == "stay":
                self.sum2 = c.convert(self.cards2)
                response_2 = "stay"

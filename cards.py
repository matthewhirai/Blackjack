import random


class Cards:
    def __init__(self):
        self.deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', "K"]*4
        for i in range(52):
            randIndex = random.randint(0, 51)
            temp = self.deck[i]
            self.deck[i] = self.deck[randIndex]
            self.deck[randIndex] = temp

    def print_hand(self, card):
        string = str(card[0])
        for i in range(1, len(card)):
            string += ", " + str(card[i])

        return string

    def dealing_cards(self, cards, number):
        for i in range(number):
            if len(self.deck) == 0:
                self.deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', "K"]*4
                for i in range(52):
                    randIndex = random.randint(0, 51)
                    temp = self.deck[i]
                    self.deck[i] = self.deck[randIndex]
                    self.deck[randIndex] = temp

            cards.append(self.deck.pop(0))

    # conversion of cards
    def convert(self, cards):
        tens = ['J', 'Q', 'K']
        t = 0
        if cards[0] == 'A' and cards[1] == 'A':
            t += 12

        if cards[0] == 'A' and cards[1] != 'A':
            cards[0], cards[1] = cards[1], cards[0]

        for i in range(len(cards)):

            if cards[i] in tens:
                t += 10

            elif cards[i] == 'A':
                if t <= 10:
                    t += 11

                elif t >= 11:
                    t += 1
            else:
                t += cards[i]
        return t

    # turns 1 and 11 to 'A' to show user
    def ace(self, cards):
        for n, i in enumerate(cards):
            if i == 1 or i == 11:
                cards[n] = 'A'
        return cards

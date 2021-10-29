import random


class Cards:
    def __init__(self):
        self.deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', "K"]*4
        for i in range(52):
            randIndex = random.randint(0, 51)
            temp = self.deck[i]
            self.deck[i] = self.deck[randIndex]
            self.deck[randIndex] = temp

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
        conversion = cards.copy()
        tens = ['J', 'Q', 'K']
        t = 0
        if conversion[0] == 'A' and conversion[1] == 'A':
            conversion[0] = 11
            conversion[1] = 1

        for i in range(len(conversion)):

            if conversion[i] in tens:
                conversion[i] = 10

            elif conversion[i] == 'A':
                conversion.pop(i)
                cards_sum = self.convert(conversion)
                if cards_sum < 10:
                    conversion.append(11)

                elif cards_sum >= 11:
                    conversion.append(1)

                elif cards_sum == 10:
                    conversion.append(11)

        t = sum(conversion)
        return t

    # turns 1 and 11 to 'A' to show user
    def ace(self, cards):
        for n, i in enumerate(cards):
            if i == 1 or i == 11:
                cards[n] = 'A'
        return cards

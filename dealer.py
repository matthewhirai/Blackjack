class Dealer:
    def __init__(self):
        self.cards = []
        self.sum = 0

    def actions(self, c):
        if self.sum == 21 and len(self.cards) == 2:
            print(f"Dealer's cards: {c.print_hand(self.cards)} = {self.sum}")
            return "blackjack"

        elif self.sum != 21:

            while self.sum <= 16:
                c.dealing_cards(self.cards, 1)
                self.sum = c.convert(self.cards)
                visible = self.cards.copy()
                visible = c.ace(visible)
                print(
                    f"Dealer's cards: {c.print_hand(self.cards)} = {self.sum}")
                if self.sum > 21:
                    self.sum = 0
                    return "stay"
                elif self.sum >= 17:
                    return "stay"

            if self.sum >= 17 and self.sum <= 21:
                print(
                    f"Dealer's cards: {c.print_hand(self.cards)} = {self.sum}")
                return "stay"

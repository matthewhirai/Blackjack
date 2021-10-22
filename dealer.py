from cards import Cards


class Dealer:
    def __init__(self):
        self.cards = []
        self.dealer_sum = 0

    def dealer_actions(self):
        bust = 0
        blackjack = 1
        stay = 2

        if self.dealer_sum != 21:

            while self.dealer_sum <= 16:
                self.cards, og_cards, self.dealer_sum = Cards.hit(
                    Cards.ace(self.cards))
                print(f"Dealer's cards: {og_cards} = {self.dealer_sum}\n")
                if self.dealer_sum > 21:
                    return bust
                elif self.dealer_sum >= 17:
                    return stay

            if self.dealer_sum >= 17 and self.dealer_sum <= 21:
                print(
                    f"Dealer's cards: {self.cards} = {self.dealer_sum}\n")
                return stay

        if self.dealer_sum == 21 and len(self.cards) == 2:
            return blackjack

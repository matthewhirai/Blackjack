from cards import Cards
from player import Player
from dealer import Dealer

if __name__ == "__main__":
    c = Cards()
    player = Player()
    dealer = Dealer()
    while True:
        player.cards.clear()
        player.cards2 = [0]
        dealer.cards.clear()
        c.dealing_cards(player.cards, 2)
        player.sum = c.convert(player.cards)
        print(f'\nMy cards: {c.print_hand(player.cards)} = {player.sum}')

        c.dealing_cards(dealer.cards, 2)
        dealer.sum = c.convert(dealer.cards)
        # need to make the last card of dealer's 'invisible' to the player
        invisible = dealer.cards[:]
        invisible.pop()
        invisible.append('*')
        print(f"Dealer's cards: {c.print_hand(invisible)}")

        player_condition = player.actions(c)
        dealer_condition = dealer.actions(c)

        # player gets blackjack
        if player_condition == "blackjack":
            if dealer_condition == "blackjack":
                print('Tie...')
            else:
                print('Blackjack!!! You win!!!')

        else:
            # no split
            if 0 in player.cards2:
                if player.sum > dealer.sum:
                    print("You win!!!")

                elif player.sum < dealer.sum:
                    print("You lose...")

                elif player.sum == dealer.sum:
                    if player.sum == 0:
                        print("You lose..")
                    else:
                        print("Push! It's a tie!")

            else:
                if player.sum > dealer.sum:
                    if player.sum2 > dealer.sum:
                        print("You win both hands!!!")
                    else:
                        print("Your 1st hand won!!!")

                elif player.sum < dealer.sum:
                    if player.sum2 < dealer.sum:
                        print("You lost both hands...")

                    elif player.sum2 > dealer.sum:
                        print("Your 2nd hand won!!!")

                    elif player.sum2 == dealer.sum:
                        print("You lost your 1st hand...")

                elif player.sum == dealer.sum:
                    if player.sum2 == dealer.sum:
                        print("Push! It's a tie for both hands!")

                    elif player.sum2 < dealer.sum:
                        print("You lost your 2nd hand...")

                    elif player.sum2 > dealer.sum:
                        print("Your 2nd hand won!!!")

        # gives the user a choice of playing again or ending it
        while True:
            answer = input('Play again? (y/n): ')
            if answer in ('y', 'n'):
                break
            else:
                print('Invalid input')
        if answer == 'y':
            continue
        else:
            print('Thank you for playing! Please come again!')
            break

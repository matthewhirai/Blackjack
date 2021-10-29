from cards import Cards
from player import Player
from dealer import Dealer

if __name__ == "__main__":
    c = Cards()
    while True:
        player = Player()
        dealer = Dealer()
        c.dealing_cards(player.cards, 2)
        player.sum = c.convert(player.cards)
        visible = player.cards.copy()
        visible = c.ace(visible)
        print(f'\nMy cards: {visible} = {player.sum}')

        c.dealing_cards(dealer.cards, 2)
        # need to make the last card of dealer's 'invisible' to the player
        invisible = dealer.cards[:]
        invisible = c.ace(invisible)

        dealer.sum = c.convert(dealer.cards)
        invisible.pop()
        invisible.append('*')
        print(f"Dealer's cards: {dealer.cards} {dealer.sum}")

        # number, player_cards_2 = player_actions(player_sum, player)
        # d_number = dealer_actions(dealer_sum, dealer)

        # player_sum = convert(player)
        # player_sum_2 = convert(player_cards_2)
        # dealer_sum = convert(dealer)

        # if player_sum_2 > 21:
        #     player_sum_2 = 0

        # # player busts
        # if number == 0 and player_sum_2 == 0:
        #     if d_number == 2 or d_number == 1:
        #         print('Bust! You lose...')

        #     elif d_number == 0:
        #         print('You both lose...')

        # # player gets blackjack
        # elif number == 1 and player_sum_2 == 0:
        #     if d_number == 1:
        #         print("Push! It's a tie!")

        #     elif d_number != 1:
        #         print('Blackjack!!! You win!')

        # # player stays
        # elif number == 2 and player_sum_2 == 0:
        #     if d_number == 0:
        #         print('You win!')

        #     elif d_number == 1:
        #         print('The dealer got blackjack. You lose...')

        #     elif d_number == 2:
        #         if player_sum > dealer_sum:
        #             print('You win!')
        #         elif player_sum < dealer_sum:
        #             print('You lose...')
        #         elif player_sum == dealer_sum:
        #             print("Push! It's a tie!")

        # # split and busts twice
        # elif number == 3:
        #     if d_number == 0 or d_number == 2:
        #         print('You lost with both hands...')

        #     elif d_number == 1:
        #         print('The dealer got blackjack. You lose...')

        # # split and stayed for both or 1st hand busts
        # elif number == 4:
        #     if d_number == 0:
        #         print('You win!')

        #     elif d_number == 1:
        #         print('The dealer got blackjack. You lose...')

        #     elif d_number == 2:

        #         # these if-statements makes it where if the 1st hand busts, its sum will go to 0
        #         if player_sum > 21:
        #             player_sum = 0

        #         if player_sum > dealer_sum:
        #             if player_sum_2 > dealer_sum:
        #                 print('Both of your hands won!')
        #             elif player_sum_2 < dealer_sum or player_sum_2 == dealer_sum:
        #                 print('Your 1st hand won!')

        #         elif player_sum < dealer_sum:
        #             if player_sum_2 < dealer_sum:
        #                 print('You lost both hands...')
        #             elif player_sum_2 > dealer_sum:
        #                 print('Your 2nd hand won!')
        #             elif player_sum_2 == dealer_sum:
        #                 print('Push for your 2nd hand, but your 1st hand lost...')

        #         elif player_sum == dealer_sum:
        #             if player_sum_2 == dealer_sum:
        #                 print("Push! Both of your hands tied with the dealer's!")
        #             elif player_sum_2 > dealer_sum:
        #                 print('Push for your 1st hand, but your 2nd hand won!')
        #             elif player_sum_2 < dealer_sum:
        #                 print('Push for your 1st hand, but your 2nd hand lost...')

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

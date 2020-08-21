import random
def dealing_cards(cards, number):
    deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', "K"]*4
    for i in range(number):
        cards.append(random.choice(deck))
    return cards

#conversion of player's cards
def convert(cards):
    new_cards = cards.copy()
    if new_cards[0] == 'A' and new_cards[1] == 'A':
        t = 12
        return t

    for i in range(len(new_cards)):

        if new_cards[i] == 'J':
            new_cards[i] = 10
            i += 1

        elif new_cards[i] == 'Q':
            new_cards[i] = 10
            i += 1

        elif new_cards[i] == 'K':
            new_cards[i] = 10
            i += 1

        elif new_cards[i] == 'A':
            new_cards.pop(i)
            card_sum = convert(new_cards)
            if card_sum < 10:
                new_cards.append(11)
                i += 1
            elif card_sum >= 11:
                new_cards.append(1)
                i += 1     
            elif card_sum == 10:
                new_cards.append(11)
                i += 1

    t = sum(new_cards)
    return t  

#split cards for player
def split(cards):
    bust = 0
    stay = 1
    bust_twice = 2

    cards_2 = cards.copy()
    cards.pop()
    cards_2.pop()
    print(f'My 1st set of cards: {cards}')
    print(f'My 2nd set of cards: {cards_2}\n')

    response = ""
    response_2 = ""
    while response != "stay":
        response = str(input("Would you like to hit or stay for your 1st hand? Type 'hit' or type 'stay'.\n"))

        if response == "hit":
            cards = dealing_cards(cards, 1)
            card_sum = convert(cards)
            print(f'My 1st set of cards: {cards} = {card_sum}')
            if card_sum > 21:
                card_sum = convert(cards)
                print('Your 1st hand busted...\n')  

                while response_2 != "stay":  # 2nd set of cards
                    response_2 = str(input("Would you like to hit or stay for your 2nd hand? Type 'hit' or type 'stay'.\n"))

                    if response_2 == "hit":
                        cards_2 = dealing_cards(cards_2, 1)
                        card_sum_2 = convert(cards_2)
                        print(f'My 2nd set of cards: {cards_2} = {card_sum_2}/n')
                        if card_sum_2 > 21:
                            card_sum_2 = convert(cards_2)
                            return bust_twice
                        elif card_sum_2 == 21:
                            return stay, cards_2 

                    elif response_2 == "stay":
                        card_sum_2 = convert(cards_2)
                        return stay, cards_2                         

        elif response == "stay":
            card_sum = convert(cards)

            while response_2 != "stay":  # 2nd set of cards
                response_2 = str(input("Would you like to hit or stay for your 2nd hand? Type 'hit' or type 'stay'.\n"))

                if response_2 == "hit":
                    cards_2 = dealing_cards(cards_2, 1)
                    card_sum_2 = convert(cards_2)
                    print(f'My 2nd set of cards: {cards_2} = {card_sum_2}')
                    if card_sum_2 > 21:
                        print('Your 2nd hand busted...\n')  
                        return bust, cards_2 
                    elif card_sum_2 == 21:
                        return stay, cards_2 

                elif response_2 == "stay":
                    card_sum_2 = convert(cards_2)
                    return stay, cards_2 

# what the player does
def player_actions(player_sum, player_cards):
    bust = 0
    blackjack = 1
    stay = 2
    bust_twice = 3
    split_stay = 4  # both hands stay or if the 1st hand busts
    player_cards_2 = [0,0]  # in case there's no split

    if player_sum != 21:

        if player_cards[0] == player_cards[1]: # when both cards are the same, the option for split comes up
                
            response = ''
            while response != "stay":
                response = str(input("Would you like to hit, stay, or split? Type 'hit', type 'stay', or type 'split'.\n"))

                if response == "hit":
                    player_cards = dealing_cards(player_cards, 1)
                    player_sum = convert(player_cards)
                    print(f'My cards: {player_cards} = {player_sum}\n')
                    if player_sum > 21:
                        player_sum = convert(player_cards)
                        return bust, player_cards_2
                    elif player_sum == 21:
                        return stay, player_cards_2


                elif response == "stay":
                    player_sum = convert(player_cards)
                    return stay, player_cards_2

                elif response == 'split':
                    s_response, player_cards_2 = split(player_cards)
                    if s_response == 0:
                        return stay, player_cards_2
                    elif s_response == 1:
                        return split_stay, player_cards_2
                    elif s_response == 2:
                        return bust_twice, player_cards_2

        elif player_cards[0] != player_cards[1]:
            response = ""
            while response != "stay":
                response = str(input("Would you like to hit or stay? Type 'hit' or type 'stay'.\n"))

                if response == "hit":
                    player_cards = dealing_cards(player_cards, 1)
                    player_sum = convert(player_cards)
                    print(f'My cards: {player_cards} = {player_sum}\n')
                    if player_sum > 21:
                        player_sum = convert(player_cards)
                        return bust, player_cards_2
                    elif player_sum == 21:
                        return stay, player_cards_2

                elif response == "stay":
                    player_sum = convert(player_cards)
                    return stay, player_cards_2
                        

    elif player_sum == 21 and len(player_cards) == 2:
        return blackjack, player_cards_2

# what the dealer does
def dealer_actions(dealer_sum, dealer_cards):
    bust = 0
    blackjack = 1
    stay = 2
    
    if dealer_sum != 21:

        for i in range(len(dealer_cards)):

            if dealer_cards[i] == 'A':

                if dealer_sum <= 16:
                    dealer_cards = dealing_cards(dealer_cards, 1)
                    dealer_sum = convert(dealer_cards)
                    print(f"Dealer's cards: {dealer_cards} = {dealer_sum}\n")
                    if dealer_sum > 21:
                        return bust
                    elif dealer_sum >= 17:
                        return stay

            elif dealer_cards[i] != 'A':

                while dealer_sum <= 16:
                    dealer_cards = dealing_cards(dealer_cards, 1)
                    dealer_sum = convert(dealer_cards)
                    print(f"Dealer's cards: {dealer_cards} = {dealer_sum}\n")
                    if dealer_sum > 21:
                        return bust
                    elif dealer_sum >= 17:
                        return stay

                if dealer_sum > 21:
                    return bust

                elif dealer_sum >= 17 and dealer_sum <=21:
                    print(f"Dealer's cards: {dealer_cards} = {dealer_sum}\n")
                    return stay

    if dealer_sum == 21 and len(dealer_cards) == 2:
        return blackjack
       
if __name__ == "__main__":
    while True:

        player_cards = []
        dealer_cards = []

        player_cards = dealing_cards(player_cards, 2)
        new_player_cards = player_cards.copy() # need to separate the converted cards from the cards that the player sees
        player_sum = convert(new_player_cards)
        print(f'My cards: {player_cards}')

        dealer_cards = dealing_cards(dealer_cards, 2)
        new_dealer_cards = dealer_cards.copy()
        dealer_sum = convert(new_dealer_cards)
        invisible = dealer_cards.copy() # need to make the last card of dealer's 'invisible' to the player
        invisible.pop()
        invisible.append('*')
        print(f"Dealer's cards: {invisible}")

        number, player_cards_2 = player_actions(player_sum, new_player_cards)
        d_number = dealer_actions(dealer_sum, new_dealer_cards)

        player_sum = convert(new_player_cards)
        player_sum_2 = convert(player_cards_2)
        dealer_sum = convert(new_dealer_cards)
        if player_sum_2 > 21:
            player_sum_2 = 0

        if number == 0 and player_sum_2 == 0: # player busts
            if d_number == 2 or d_number == 1:
                print('Bust! You lose...')

            elif d_number == 0:
                print('You both lose...')

    
        elif number == 1 and player_sum_2 == 0: # player gets blackjack
            if d_number == 1:
                print("Push! It's a tie!")

            elif d_number != 1:
                print('Blackjack!!! You win!')


        elif number == 2 and player_sum_2 == 0: # player stays
            if d_number == 0:
                print('You win!')

            elif d_number == 1:
                print('The dealer got blackjack. You lose...')

            elif d_number == 2:
                if player_sum > dealer_sum:
                    print('You win!')
                elif player_sum < dealer_sum:
                    print('You lose...')
                elif player_sum == dealer_sum:
                    print("Push! It's a tie!")


        elif number == 3: # split and busts twice
            if d_number == 0 or d_number == 2:
                print('You lost with both hands...')

            elif d_number == 1:
                print('The dealer got blackjack. You lose...')

        
        elif number == 4: # split and stayed for both or 1st hand busts
            if d_number == 0:
                print('You win!')

            elif d_number == 1:
                print('The dealer got blackjack. You lose...')

            elif d_number == 2:

                # these if-statements makes it where if a hand is over 21/busts, its sum will go to 0
                if player_sum > 21:
                    player_sum = 0


                if player_sum > dealer_sum:
                    if player_sum_2 > dealer_sum:
                        print('Both of your hands won!')
                    elif player_sum_2 < dealer_sum:
                        print('Your 1st hand won!')
                    elif player_sum_2 == dealer_sum:
                        print('Your 1st hand won!')
                

                elif player_sum < dealer_sum:
                    if player_sum_2 < dealer_sum:
                        print('You lost both hands...')
                    elif player_sum_2 > dealer_sum:
                        print('Your 2nd hand won!')
                    elif player_sum_2 == dealer_sum:
                        print('You lost your 1st hand, but tied for your 2nd hand.')

                elif player_sum == dealer_sum:
                    if player_sum_2 == dealer_sum:
                        print("Push! Both of your hands tied with the dealer's!")
                    elif player_sum_2 > dealer_sum:
                        print('Push for your 1st hand, but your 2nd hand won!')
                    elif player_sum_2 < dealer_sum:
                        print('Push for your 2nd hand, but your 1st hand lost...')

        # gives the user a choice of playing again or ending it
        while True:
            answer = input('Play again? (y/n): ')
            if answer in ('y', 'n'):
                break
                print('Invalid input')
        if answer == 'y':
            continue
        else:
            print('Thank you for playing! Please come again!')
            break
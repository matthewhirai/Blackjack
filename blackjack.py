import random

def dealing_cards(cards, number):
    deck = []
    if len(deck) == 0:
        deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', "K"]*4
    for i in range(number):
        cards.append(random.choice(deck))
    return cards

#conversion of player's cards
def convert(cards):
    tens = ['J', 'Q', 'K']
    t = 0
    if cards[0] == 'A' and cards[1] == 'A':
        cards[0] = 11
        cards[1] = 1

    for i in range(len(cards)):

        if cards[i] in tens:
            cards[i] = (10)

        elif cards[i] == 'A':
            cards.pop(i)
            cards_sum = convert(cards)
            if cards_sum < 10:
                cards.append(11)

            elif cards_sum >= 11:
                cards.append(1)
   
            elif cards_sum == 10:
                cards.append(11)

    t = sum(cards)
    return t

#turns 1 and 11 to 'A' to show user
def ace(cards):
    for n, i in enumerate(cards):
        if i == 1 or i == 11:
            cards[n] = 'A'
    return cards

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
                        print(f'My 2nd set of cards: {cards_2} = {card_sum_2}\n')
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

#adds a card to hand
def hit(cards):
    cards = dealing_cards(cards, 1)
    og_cards = cards.copy()
    og_cards = ace(og_cards)
    card_sum = convert(cards)
    return cards, og_cards, card_sum

# what the player does
def player_actions(player_sum, player_cards):
    bust = 0
    blackjack = 1
    stay = 2
    bust_twice = 3
    split_stay = 4  # both hands stay or if the 1st hand busts
    player_cards_2 = [0,0]  # in case there's no split

    if player_sum != 21:

        response = ''
        if player_cards[0] == player_cards[1]: # when both cards are the same, the option for split comes up
                
            while response != "stay":
                response = str(input("Would you like to hit, stay, or split? Type 'hit', type 'stay', or type 'split'.\n"))

                if response == "hit":
                    player_cards, og_cards, player_sum = hit(ace(player_cards))
                    print(f'My cards: {og_cards} = {player_sum}\n')
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
            while response != "stay":
                response = str(input("Would you like to hit or stay? Type 'hit' or type 'stay'.\n"))

                if response == "hit":
                    player_cards, og_cards, player_sum = hit(player_cards)
                    print(f'My cards: {og_cards} = {player_sum}\n')
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

        while dealer_sum <= 16:
            dealer_cards, og_cards, dealer_sum = hit(ace(dealer_cards))
            print(f"Dealer's cards: {og_cards} = {dealer_sum}\n")
            if dealer_sum > 21:
                return bust
            elif dealer_sum >= 17:
                return stay

        if dealer_sum >= 17 and dealer_sum <=21:
            print(f"Dealer's cards: {dealer_cards} = {dealer_sum}\n")
            return stay

    if dealer_sum == 21 and len(dealer_cards) == 2:
        return blackjack
       
if __name__ == "__main__":
    while True:

        player= []
        dealer = []

        player = dealing_cards(player, 2)
        visible = player.copy()
        visible = ace(visible)
        player_sum = convert(player)
        print(f'\nMy cards: {visible}')

        dealer= dealing_cards(dealer, 2)
        invisible = dealer.copy() # need to make the last card of dealer's 'invisible' to the player
        invisible = ace(invisible)
        dealer_sum = convert(dealer)
        invisible.pop()
        invisible.append('*')
        print(f"Dealer's cards: {dealer}")

        number, player_cards_2 = player_actions(player_sum, player)
        d_number = dealer_actions(dealer_sum, dealer)

        player_sum = convert(player)
        player_sum_2 = convert(player_cards_2)
        dealer_sum = convert(dealer)
        
        if player_sum_2 > 21:
            player_sum_2 = 0

        # player busts
        if number == 0 and player_sum_2 == 0: 
            if d_number == 2 or d_number == 1:
                print('Bust! You lose...')

            elif d_number == 0:
                print('You both lose...')

        # player gets blackjack
        elif number == 1 and player_sum_2 == 0: 
            if d_number == 1:
                print("Push! It's a tie!")

            elif d_number != 1:
                print('Blackjack!!! You win!')

        # player stays
        elif number == 2 and player_sum_2 == 0: 
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

        # split and busts twice
        elif number == 3: 
            if d_number == 0 or d_number == 2:
                print('You lost with both hands...')

            elif d_number == 1:
                print('The dealer got blackjack. You lose...')

        # split and stayed for both or 1st hand busts
        elif number == 4: 
            if d_number == 0:
                print('You win!')

            elif d_number == 1:
                print('The dealer got blackjack. You lose...')

            elif d_number == 2:

                # these if-statements makes it where if the 1st hand busts, its sum will go to 0
                if player_sum > 21:
                    player_sum = 0

                if player_sum > dealer_sum:
                    if player_sum_2 > dealer_sum:
                        print('Both of your hands won!')
                    elif player_sum_2 < dealer_sum or player_sum_2 == dealer_sum:
                        print('Your 1st hand won!')
                
                elif player_sum < dealer_sum:
                    if player_sum_2 < dealer_sum:
                        print('You lost both hands...')
                    elif player_sum_2 > dealer_sum:
                        print('Your 2nd hand won!')
                    elif player_sum_2 == dealer_sum:
                        print('Push for your 2nd hand, but your 1st hand lost...')

                elif player_sum == dealer_sum:
                    if player_sum_2 == dealer_sum:
                        print("Push! Both of your hands tied with the dealer's!")
                    elif player_sum_2 > dealer_sum:
                        print('Push for your 1st hand, but your 2nd hand won!')
                    elif player_sum_2 < dealer_sum:
                        print('Push for your 1st hand, but your 2nd hand lost...')

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
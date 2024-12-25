import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]*4


def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        hand.append(card)
    return hand

def play_again(number_of_chips):
    again = input("Du har nå: " + str(number_of_chips) + " chips. Vil du spille igjen?: j/n: ")
    if again == "j":
        next_round(number_of_chips)
    else:
        print("Hade!")
        exit()

def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total += 10
        elif card == "A":
            if total >= 11: total+= 1
            else: total += 11
        else: total += card
    return total

def hit(hand):
    card = deck.pop()
    hand.append(card)
    return hand

def inputBet():
    bet = int(input("Hvor mye vil du satse? "))
    return bet 


def print_results(dealer_hand, player_hand):
    print("Dealeren har " + str(dealer_hand) + " totalt " + str(total(dealer_hand)))
    print("Du har " + str(player_hand) + " totalt " + str(total(player_hand)))

def blackjack(dealer_hand, player_hand, bet):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Gratulerer, du fikk Blackjack!\n")
        return bet * 2
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)        
        print("Du taper, dealeren fikk Blackjack.\n")
        return 0-bet
    return 0

def score(dealer_hand, player_hand, bet):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Gratulerer, du fikk Blackjack!\n")
        return bet * 2
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)        
        print("Du taper, dealeren fikk Blackjack..\n")
        return 0-bet
    elif total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Busted\n")
        return 0-bet
    elif total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)               
        print("Dealer bustet. Du vinner!\n")
        return bet
    elif total(player_hand) < total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Du fikk lavere score enn dealeren, du taper!\n")
        return 0-bet
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)               
        print("Du fikk høyere score enn dealeren, du vinner!\n")
        return bet
    elif total(dealer_hand) == total(player_hand):
        print("Det ble likt, ingen vinner\n")
        return 0   

def game():
    total_chips = int(input("Antall start chips? "))
    print("\nDu har: " + str(total_chips) + " chips.")
    next_round(total_chips)
    

def next_round(total_chips):
    choice = 0
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    bet = inputBet()
    print("Dealeren viser " + str(dealer_hand[0]))
    print("Du har " + str(player_hand) + " totalt " + str(total(player_hand)))
    win = blackjack(dealer_hand, player_hand, total_chips)
    if win == 0:
        quit=False
        while not quit:
            choice = input("Vil du [H]it, [S]tand, eller [Q]uit: ").lower()
            if choice == "h":
                hit(player_hand)
                print(player_hand)
                if total(player_hand)>21:
                    total_chips += score(dealer_hand, player_hand, bet)
                    print("Du har nå: " + str(total_chips) + " chips!\n") 
                    play_again(total_chips)
            elif choice == "s":
                while total(dealer_hand)<17:
                    hit(dealer_hand)
                    print(dealer_hand)
                    if total(dealer_hand)>21:
                        total_chips += score(dealer_hand, player_hand, bet)
                        print("Du har nå: " + str(total_chips) + " chips!\n") 
                        print("Dealer bustet, du vinner!")
                        play_again(total_chips)
                total_chips += score(dealer_hand, player_hand, bet)
                print("Du har nå: " + str(total_chips) + " chips!\n") 
                play_again(total_chips)
            elif choice == "q":
                print("Hade!")
                quit=True
                exit()
    else:
        total_chips += win
        print("Du har nå: " + str(total_chips) + " chips!!\n") 
        play_again(total_chips)

if __name__ == "__main__":
   game()
import random

# Create 2 decks for the games
def create_decks(num_decks=2):
    deck = []
    for _ in range(num_decks):
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for value in range(2, 11):
                deck.append((str(value), suit))
            for face in ['Jack', 'Queen', 'King', 'Ace']:
                deck.append((face, suit))
    random.shuffle(deck)
    return deck

# Deal the hands
def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card, suit in hand:
        if card in ['Jack', 'Queen', 'King']:
            value += 10
        elif card == 'Ace':
            num_aces += 1
            value += 11
        else:
            value += int(card)
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

# Print the cards
def print_hand(hand, hidden=False):
    if hidden:
        print(f"Dealer's hand: [{hand[0][0]} of {hand[0][1]}, Hidden]")
    else:
        print("Hand: " + ", ".join(f"{card} of {suit}" for card, suit in hand))

# Check if player wants to hit or stay
def player_turn(deck, dealer_hand):
    hand = [deck.pop(), deck.pop()]
    print("Your hand:", ", ".join(f"{card} of {suit}" for card, suit in hand))
    
    while True:
        if calculate_hand_value(hand) > 21:
            print("Busted! You lose.")
            return hand
        choice = input("Do you want to hit? (Y/N): ").lower()
        if choice == 'y':
            hand.append(deck.pop())
            print("Your hand:", ", ".join(f"{card} of {suit}" for card, suit in hand))
        elif choice == 'n':
            break
        else:
            print("Invalid choice, please choose 'Y' or 'N'.")
    return hand

# Dealer's turn, dealer has to hit if lower than 17
def dealer_turn(deck, dealer_hand):
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    return dealer_hand

# Play the game
def play_single_hand(deck):
    dealer_hand = [deck.pop(), deck.pop()]
    print_hand(dealer_hand, hidden=True)

    player_hand = player_turn(deck, dealer_hand)
    if calculate_hand_value(player_hand) > 21:
        return player_hand, []

    dealer_hand = dealer_turn(deck, dealer_hand)
    
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    print_hand(player_hand)
    print_hand(dealer_hand)

    if dealer_value > 21 or player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")
    
    return player_hand, dealer_hand

# Main function
def play_blackjack():
    deck = create_decks()
    discard_pile = []

    while True:
        player_hand, dealer_hand = play_single_hand(deck)
        discard_pile.extend(player_hand)
        discard_pile.extend(dealer_hand)

        if len(deck) < 20:  # If the deck is running low, reshuffle discard pile into deck
            deck.extend(discard_pile)
            random.shuffle(deck)
            discard_pile = []

        play_again = input("Do you want to play again? (Y/N): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    play_blackjack()

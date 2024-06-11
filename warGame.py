# Name: Nana Kwasi Owusu
# Date: 2 March, 2024
# Program Description: This is a game that is similar to the popular War Card Game. The players use the cards in their decks to battle until one person runs out of cards.

#This module allows the program to exit when the number of cards in the deck are not equal 
import sys

#This function makes the players battle every time when they draw a card. The player who plays a bigger card gets the other player's card. If the cards are the same, the warTie function is called.
def war(deck1, deck2):
    if len(deck1) == 0 or len(deck2) == 0:
        if len(deck1) > len(deck2):
            print('Player 1 is victorious!')
        else:
            print('Player 2 is victorious!')
        return
    
    p1 = deck1.pop(0)
    p2 = deck2.pop(0)
    print(f'Battle: Player 1 played {p1}')
    print(f'Battle: Player 2 played {p2}')

    if p1 > p2:
        print('Player 1 won this battle.')
        deck1.append(p1)
        deck1.append(p2)
    elif p2 > p1:
        print('Player 2 won this battle.')
        deck2.append(p1)
        deck2.append(p2)
    else:
        print('Players tie on this battle.')
        print('War is declared.')
        warTie(deck1, deck2, [p1, p2])

    print(f"After Battle: Player 1 Deck contains {deck1}")
    print(f"After Battle: Player 2 Deck contains {deck2}")
    war(deck1, deck2)
    
#This is a recursive function that handles the wars. The function checks whether both players have sufficient cards (base case), matches the face-up cards and determines who the winner is. If there is a tie, it recursively calls itself.
def warTie(deck1, deck2, warCards):
    if len(deck1) < 2 or len(deck2) < 2:
        if len(deck1) > len(deck2):
            print('Player 2 is out of cards. Player 1 is victorious!')
        else:
            print('Player 1 is out of cards. Player 2 is victorious!')

        return

    p1FaceDown = deck1.pop(0)
    p2FaceDown = deck2.pop(0)
    print(f'War: Player 1 face down card: {p1FaceDown}')
    print(f'War: Player 2 face down card: {p2FaceDown}')

    p1FaceUp = deck1.pop(0)
    p2FaceUp = deck2.pop(0)
    print(f'War: Player 1 face up card: {p1FaceUp}')
    print(f'War: Player 2 face up card: {p2FaceUp}')

    warCards += [p1FaceDown, p2FaceDown, p1FaceUp, p2FaceUp]

    if p1FaceUp > p2FaceUp:
        print('War: Player 1 won this war')
        deck1 += warCards
    elif p2FaceUp > p1FaceUp:
        print('War: Player 2 won this war')
        deck2 += warCards
    else:
        print('War: Another Tie. War is declared again.')
        warTie(deck1, deck2, warCards)
        
#Main part of the script 
if __name__ == "__main__":
    print('Prepare for War (The Card Game).')
    deck1 = input('Enter your cards from top to bottom. Put spaces between values.\n').split()
    deck2 = input('Enter your cards from top to bottom. Put spaces between values.\n').split()
    
    player1Deck = []
    for card in deck1:
        player1Deck.append(int(card))
    player2Deck = []
    for card in deck2:
        player2Deck.append(int(card))
        
    if len(player1Deck) != len(player2Deck):
        print('Cannot play if decks have different numbers of cards.')
        sys.exit(0)
    else:
        print('Player 1 Deck: ',player1Deck)
        print('Player 2 Deck: ',player2Deck)
        war(player1Deck,player2Deck)
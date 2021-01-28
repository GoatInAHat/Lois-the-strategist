__author__ = 'Juan Calderon'


 # BLACKJACK
 # ---------
 #
 # This is a text-based Blackjack game program. One player plays with the dealer (the computer).
 # The player starts with 100 chips and must bet at least 1 chip each hand.
 # This game is played using a french deck of 52 cards
 # Face cards count as 10 points, and ace cards count as either 1 or 11 depending on the situation.
 # Other cards count as their numeric values.
 # The game begins when the dealer, after shuffling the cards,  places the first card of the deck
 # into the discard tray, face down.
 # The player places his or her wagers. Next, the first card goes to the player, and the second to the dealer.
 # A second card goes to the player and another to the dealer, but this time face down (hold card).
 # From that moment on, the player may decide to be hit to receive a new card or stand.
 # When the player stands, the dealer faces up the hold card and hits until his or her hand is 17 or greater.
 # If both player and dealer make 21 adding the numbers of their cards (final score), both are tied (push),
 # and the player loses no money.
 # If the final score of the player is greater than dealer's and lesser or equal than 21, the player wins 1:1
 # If dealer's final score is greater than 21, the player wins (1:1)


# Imports the "random module" to further us the "random.shuffle" function
import random


# CONSTANT DEFINITIONS:
# --------------------

SPADE = unichr(9824) #Unicode for spade
HEART = unichr(9829) #Unicode for heart
DIAMOND = unichr(9830) # Unicode for  diamond
CLUB = unichr(9827) #Unicode for club
SOFT = 17 # Integer used to compare whether the dealer cards add up 17
BL_JCK = 21 # Integer used to compare whether the player or dealer cards add up 21

# DECK definition as a dictionary where each key is a string representing a card and the associated value is a list
# containing in the first position of the list the numeric value of the card, and in the second position a string to
# to display the card on the console.

DECK = {"a_spade": [11,"A"+SPADE], "c2_spade": [2, "2"+SPADE], "c3_spade": [3, "3"+SPADE], "c4_spade": [4, "4"+SPADE], \
        "c5_spade": [5, "5"+SPADE], "c6_spade": [6, "6"+SPADE], "c7_spade": [7, "7"+SPADE],"c8_spade": [8, "8"+SPADE], \
        "c9_spade": [9, "9"+SPADE], "c10_spade": [10, "10"+SPADE], "j_spade": [10, "J"+SPADE], \
        "q_spade": [10, "Q"+SPADE], "k_spade": [10, "K"+SPADE],\
        "a_heart": [11,"A"+HEART], "c2_heart": [2, "2"+HEART], "c3_heart": [3, "3"+HEART], "c4_heart": [4, "4"+HEART], \
        "c5_heart": [5, "5"+HEART], "c6_heart": [6, "6"+HEART], "c7_heart": [7, "7"+HEART],"c8_heart": [8, "8"+HEART], \
        "c9_heart": [9, "9"+HEART], "c10_heart": [10, "10"+HEART], "j_heart": [10, "J"+HEART], \
        "q_heart": [10, "Q"+HEART], "k_heart": [10, "K"+HEART],\
        "a_diamond": [11,"A"+DIAMOND], "c2_diamond": [2, "2"+DIAMOND], "c3_diamond": [3, "3"+DIAMOND], "c4_diamond": [4, "4"+DIAMOND], \
        "c5_diamond": [5, "5"+DIAMOND], "c6_diamond": [6, "6"+DIAMOND], "c7_diamond": [7, "7"+DIAMOND],"c8_diamond": [8, "8"+DIAMOND], \
        "c9_diamond": [9, "9"+DIAMOND], "c10_diamond": [10, "10"+DIAMOND], "j_diamond": [10, "J"+DIAMOND], \
        "q_diamond": [10, "Q"+DIAMOND], "k_diamond": [10, "K"+DIAMOND],\
        "a_club": [11,"A"+CLUB], "c2_club": [2, "2"+CLUB], "c3_club": [3, "3"+CLUB], "c4_club": [4, "4"+CLUB], \
        "c5_club": [5, "5"+CLUB], "c6_club": [6, "6"+CLUB], "c7_club": [7, "7"+CLUB],"c8_club": [8, "8"+CLUB], \
        "c9_club": [9, "9"+SPADE], "c10_club": [10, "10"+SPADE], "j_club": [10, "J"+SPADE], \
        "q_club": [10, "Q"+CLUB], "k_club": [10, "K"+CLUB]

        }

# DATA DEFINITIONS:
# ----------------

# Card is string
# Represents each individual card name of the deck of cards. Example: "a_diamond" corresponds to the ace of diamonds.

# Deck_list is list
# List containing only strings of card names. Example: player = ["c5_club", "q_heart"]

# Hit is tuple
# The tuple contains 2 lists. Example: ([updated player's list], [updated deck of cards' list])


# Chips is integer
# Represents a range of integer numbers between 0 and 100. Example: chips = 100


# Hand_option is list
# This type of data presents a list of strings of the following hand options available for the player:
# - "quit"
# - "stand"
# - "hit"


# Game_option is list
# This type of data presents a list of strings of the following game options available for the player:
# - "continue"
# - "quit"



# Text_message is string !!!
# This are strings involving visual representation of the card and complementary information to identify if the
# cards belong to the player or the dealer


# FUNCTIONS:
# ---------

#create_deck_list
#Dictionary -> Deck_list
#Consumes DECK, the deck of cards dictionary, and produces a list of card names.

def create_deck_list(DECK):
    deck_list = []
    for x in DECK:
        deck_list.append(x)
    return deck_list

# hitting
# Deck_list, Deck_list -> Hit
# Consumes a list of cards corresponding to either the player or the dealer and a deck of cards list, appends a card
# to the player or dealer lists and pops a card of the deck of cards list. Produces a tuple containing the updated
# version of both lists.

def hitting(pl_dea_deck, deck_list):
        pl_dea_deck.append(deck_list.pop(0))
        return (pl_dea_deck, deck_list)



# deck_shuffling
# Deck_list -> Deck_list
# Consumes a deck of cards list and produces a shuffled version using the random.shuffle function

def deck_shuffling(deck_list1):
        return random.shuffle(deck_list1)


# is_more
# Deck_list, Dictionary, Integer -> Boolean
# Consumes a player or dealer cards list. the deck of cards dictionary, DECK, and an integer (SOFT=17 or BL_JK=21).
# It produces a "true" if the sum of the numbers representing the cards on the list adds up more than the integer's
# value (SOFT=17 or BL_JK=21). Produces "false" otherwise.

def is_more(deck_list1, DECK, integer1):
        return cards_sum(deck_list1, DECK)>integer1


# is_less
# Deck_list, Dictionary, Integer -> Boolean
# Consumes a player or dealer cards list. the deck of cards dictionary, DECK, and an integer (SOFT=17 or BL_JK=21).
# It produces a "true" if the sum of the numbers representing the cards on the list adds up less than the integer's
# value (SOFT=17 or BL_JK=21). Produces "false" otherwise.

def is_less(deck_list1, DECK, integer1):
        return cards_sum(deck_list1, DECK)<integer1


# is_equ
# Deck_list, Dictionary, Integer -> Boolean
# Consumes a player or dealer cards list. the deck of cards dictionary, DECK, and an integer (SOFT=17 or BL_JK=21).
# It produces a "true" if the sum of the numbers representing the cards on the list adds up the integer's value
# (SOFT=17 or BL_JK=21). Produces "false" otherwise.

def is_equ(deck_list1, DECK, integer1):
        return cards_sum(deck_list1, DECK)==integer1



# cards_sum
# Deck_list, Dictionary -> Integer
# This is a helper function. Consumes a deck of cards list and a deck of cards dictionary, DECK. The DECK provides
# information of cards value and each card name on the deck of cards list serves as a key. This function produces an
# integer resulting of summing the card values.

def cards_sum(deck_list1, DECK):
        card_sum = 0
        for x in deck_list1:
            card_sum+=DECK[x][0]
        return card_sum



# ace_is_11 !!!
# Card, integer



# is_tied !!!
# Deck_list, Deck_list -> Boolean
# consumes the lists of cards corresponding to player and dealer, and in the case of each list adds up 21 separately
# produces a "True". Produces a "False" otherwise.

def is_tied(deck_list1):
        pass


# standing !!!
# Hand_option -> Boolean
# Receives a string containing a hand option and produces "True" if the string is "hit" or "False" otherwise.

def standing(string_val):
        pass

# scoring !!!
# list -> integer


def scoring(deck_list):
        pass

# results_presentation !!!

# state_printing
# Deck_list, Boolean -> Text_message
# Consumes player or dealer lists as well as a boolean variable (dealer_is) that identifies whether the list of cards
# to print belongs to the dealer or not. Produces the printing of a text message containing information of the current
# state of player or dealer. In the case of the dealer, this function  prints an X in the place of the face down card
# and flips it over when the player stands.

def state_printing(pl_dea_list, dealer_is):
        deck_list_aux = []
        for x in pl_dea_list:
                deck_list_aux.append(DECK[x][1])
        print player_or_dealer(dealer_is), x_in_dealer(deck_list_aux, dealer_is)


# player_or_dealer
# Boolean -> String
# This is a helper function to ease the process of state printing. It Consumes a boolean variable that when set
# to True produces the message "Dealer: ". Otherwise, produces "Player: "

def player_or_dealer(dealer_is):
    if dealer_is:
        return "Dealer: "
    else:
        return "Player: "


# x_in_dealer
# This is a helper function to ease the process of state printing. It consumes a player or dealer card list and
# a boolean variable that when set to True tells that the card list belongs to the dealer. Only when the card list
# belongs to the dealer and the dealer has only 2 cards, the second one corresponds to the face down card that is
# printed as an "X".

def x_in_dealer(deck_list_aux, dealer_is):

    if not dealer_is or len(deck_list_aux)>2 or len(deck_list_aux)<2:
        return " ".join(deck_list_aux)

    else:
        deck_list_aux[1] = "X"
        return " ".join(deck_list_aux)

#data_acquisition?...



# betting
# integer, list -> list

def betting(int, list1):
        pass



# to_discard_tray
# Deck_list -> Card, Deck_list?...


# is_blackjack

# min_chips_covered
# integer -> boolean


# Blackjack_hand
# Chips -> Chips
# This function receives and amount of chips to bet in a particular hand and receives the resulting chip amount after
# wining of losing. If the player wins the amount is positive. Otherwise it is negative

def Blackjack_hand(chips):
        # Initial conditions for the Blackjack hand
        player = [] # variable of Deck_list type representing the player
        dealer = [] # variable of Deck_list type representing th dealer
        deck_list = [] # variable of Deck_list type representing the deck of cards
        hold_card = [] # variable of Deck_list type representing the face down card of the dealer
        discard_tray = [] # variable of Deck_list type representing the discarded card
        hit = ()

        dealer_is = False # Boolean variable stating whether it is the dealer or not
        hand_chips = 0 # variable of integer type containing chips won (positive integers)  or lost (negative integers)
        bet = 0 # variable of integer type representing the number of chips to bet (0< bet<chips)
        quit_hand = False
        hit_hand = False
        stand_hand = False # Boolean variable stating whether the player stands or not
        player_wins = False
        hand_option = ""
        hand_options = ["hit", "stand", "quit" ] # variable of list type containing hand menu options.


        # Deck preparation:
        deck_list = create_deck_list(DECK) #simulates a deck of cards using a list of their names
        deck_shuffling(deck_list) # produces a shuffled version of the deck of cards


        # The dealer places the first card of the deck on the discard tray, face down.
        hit = hitting(discard_tray, deck_list)
        discard_tray = hit[0]
        deck_list = hit[1]

        print "discard tray: ", discard_tray

        # The player bets:
        while bet<1 or bet>chips:

                bet = int(raw_input("Please, place your wager (1-chips): " ))

        print "Your wager:", bet

        # First card goes to the player:
        hit = hitting(player, deck_list)

        player = hit[0]

        deck_list = hit[1]



        # Second card goes to the dealer:

        hit = hitting(dealer, deck_list)

        dealer = hit[0]

        deck_list = hit[1]



        # Third card goes to the player:
        hit = hitting(player, deck_list)

        player = hit[0]

        deck_list = hit[1]



        # Fourth card goes to the dealer:

        hit = hitting(dealer, deck_list)

        dealer = hit[0]

        deck_list = hit[1]

        state_printing(player, False)
        state_printing(dealer, True)
        print 'The "X" is the "Hold Card"'
        if is_equ(player, DECK, BL_JCK):
                print "player above 21 *"
                quit_hand = True



        # Player hits, stands or quits:
        while not quit_hand:
                while not hand_option in hand_options :

                        hand_option = raw_input('Please, enter "hit", "stand" or "quit" : ' )


                if  hand_option=="hit":

                        hand_option = ""

                        # The player hits:

                        hit = hitting(player, deck_list)

                        player = hit[0]

                        deck_list = hit[1]

                        state_printing(player, False)
                        state_printing(dealer, True)
                        if is_more(player, DECK, BL_JCK):
                                print "player above 21"
                                break


                elif hand_option=="stand":

                        while is_less(dealer,DECK, SOFT):
                                hit = hitting(dealer, deck_list)
                                dealer = hit[0]
                                deck_list = hit[1]
                        state_printing(player, False)
                        state_printing(dealer, True)



                        break

                else:
                        print "quitting"

                        hands_chips = -bet
                        return hands_chips



        if     cards_sum(player,DECK)>BL_JCK:
                print "Player loses: ", bet
                hand_chips = -bet
        elif   cards_sum(player, DECK)>cards_sum(dealer, DECK) and is_less(player,DECK, BL_JCK):
                print "-less 21- the player wins: ", bet
                hand_chips = bet
        elif cards_sum(player, DECK)>cards_sum(dealer, DECK) and is_equ(player, DECK, BL_JCK):
                print "-= 21- the player wins: ", bet
                hand_chips = bet
        elif cards_sum(player, DECK)<cards_sum(dealer, DECK) and is_less(dealer, DECK, BL_JCK):
                print "-less 21- Player loses: ", bet
                hand_chips = -bet
        elif cards_sum(player, DECK)==cards_sum(dealer, DECK) and is_less(player, DECK, BL_JCK):
                print "Both Player and Dealer are tied"
                hands_chips = 0
        elif cards_sum(player, DECK)==cards_sum(dealer, DECK) and is_equ(player, DECK, BL_JCK):
                print "-21-Both Player and Dealer are tied"
                hands_chips = 0
        elif cards_sum(player, DECK)<cards_sum(dealer, DECK) and is_more(dealer, DECK, BL_JCK):
                print "< the player wins"
                hands_chips = bet

        else:
                print "else, Player loses: ", bet
                hands_chips= -bet

        #FINAL:

        print "hand over"
        return hand_chips


# Blackjack_game
# Chips -> Chips
# This is the main Blackjack game program to run. Consumes chips to bet and produces the total of chips left after
# playing
def Blackjack_game(chips):

        chips_count = [] # variable of List type utilized to contain the initial bet and subsequent results of the game
        game_options = ["start", "quit"] # variable of Game_option type representing the available Player menu options
        print "**** Blackjack welcomes you! ****"
        print "To start playing, you need at least 100 chips "

# The following while loop ensures that the player starts the game with an amount of chips greater or equal than 100
# and provides the player with the option for quitting the game
        while chips <100:

                chosen_option = ""
                while not chosen_option in game_options:

                        chosen_option = raw_input('write in lowercase "start" for playing or "quit" for leaving the game: ')

                if chosen_option == "quit":
                        break
                chips = int(raw_input("Please enter the initial amount of chips: " ))

        else:
                while True:
                        chosen_option = ""
                        while not chosen_option in game_options:
                                chosen_option = raw_input('New hand? "start" for playing or "quit" for leaving the game: ')
                        if chosen_option == "quit":
                                break
                        chips_count.append(Blackjack_hand(chips))


        print "Starting chips:", chips
        print "Final Score: ", chips_count
        print "Thanks for your visit"



#-----------------------------------------------
#RUNNING THE PROGRAM:

chips = 0

Blackjack_game(chips)
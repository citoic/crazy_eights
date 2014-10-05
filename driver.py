# CS 156 homework 1 
# 6 October 2014
# Katharine Brinker and Edward Ciotic

import sys
import copy
import random
import crazy_eights

deck = []
hand_player = []
hand_computer = []
history = []
player_turn = True
continue_game = True #for exit of game loop
face_up_card = -1
suit = 0
partial_state = (face_up_card, suit, hand_computer, history)
state = (deck, hand_player, partial_state)
key = """
          A   2   3   4   5   6   7   8   9   10  J   Q   K
Spade     0   1   2   3   4   5   6   7   8   9   10  11  12
Heart     13  14  15  16  17  18  19  20  21  22  23  24  25
Diamond   26  27  28  29  30  31  32  33  34  35  36  37  38
Club      39  40  41  42  43  44  45  46  47  48  49  50  51
"""


#initialize deck with ints form 0-51
for i in range(0,52):
    deck.append(i)

#shuffle deck of cards/ may not need since random.shuffe() is a thing
def shuffle_deck(deck):
    length = (len(deck) / 2) - 1
    length = int(length)
    for n in range(0, 10000):
        index = random.randint(0,length)
        index2 = index + length
        temp = deck[index2]
        deck[index2] = deck[index]
        deck[index] = temp

    temp = deck[51]
    i = random.randint(0,length)
    deck[51] = deck[i]
    deck[i] = temp

#initialize hand. List 0-51 where 0 represents no card in hand, 1 represents card in hand
for i in range(0,52):
    hand_computer.append(0)
    hand_player.append(0)

#asks user for input and returns a tuple as specified
def input_to_tuple():
    var = raw_input("Please enter your move: ")
    #print "you entered", var
    var = var.replace(',','')
    var = var.replace('(','')
    var = var.replace(')','')
    #print var
    var = [int(n) for n in var]
    tup = tuple(var)
    return tup

#used by display hand
def extract_cards(list):
    text = ""
    for n, i in enumerate(list):
        if i == 1:
            if n == 0:
                text += "A, " 
            elif n == 10:
                text += "J, "
            elif n == 11:
                text += "Q, "
            elif n == 12:
                text += "K, "  
            else:
                text += str(n + 1) + ", "
    text = text.strip() #remove trailing whitepsace
    text = text.strip(',') #remove trailing comma
    return text


#used to display to user what cards are in their hand
def display_hand(hand):
    s = hand[0:13]           
    h = hand[13:26]
    d = hand[26:39]
    c = hand[39:52]
    print "Cards in your hand: "
    print "Spade: " + extract_cards(s)
    print "Heart: " + extract_cards(h)
    print "Diamond: " + extract_cards(d)
    print "Club: " + extract_cards(c)

def update_suit():
    if face_up_card < 13:
        suit = 0
    elif face_up_card < 26:
        suit = 1
    elif face_up_card < 39:
        suit = 2
    else:
        suit = 3

def check_valid():
    move = history[len(history) - 1]
    if len(move) != 4:
        return False
    #other checks

def player_move():
    display_hand(hand_player)
    print "face up card is " + str(face_up_card)
    history.append(input_to_tuple())
    while not check_valid():
        print "Input was not correct, please enter correct input"
        history.append(input_to_tuple())

def computer_move():



#display_hand(hand_player)
#ask who plays first
usr_input = raw_input("Would you like to play [F]irst or [S]econd: ")
if usr_input == "S":
    player_turn = False

print "Key for face up card and input:"
print key

#initialize game
#suffle deck
random.shuffle(deck)

#deal cards to players 
for x in range(0,8):
    card = deck.pop()
    hand_player[card] = 1

for x in range(0,8):
    card = deck.pop()
    hand_computer[card] = 1

#get first face up card    
face_up_card = deck.pop()
update_suit()

#first move logic before entering the game loop
if player_turn:
    player_move()
    #then enter game loop 
#else:
    #player second



#game loop
while continue_game:
    if game_over():
        print "gave over"
        #TODO: check who won the game
        break
    if player_turn:
        player_move()
        #anything else that needs to be done per move
    else:
        computer_move()












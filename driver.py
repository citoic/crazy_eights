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
winner = -1

#initialize   deck.append(i)deck with ints form 0-51
for i in range(0,52):
  

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
    var = var.replace('(','')
    var = var.replace(')','')
    li =  [int(x) for x in var.split(',')]
    tup = tuple(li)
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
    if (face_up_card % 13) == 7:
        move = history[-1]
        suit = move[2]
    elif face_up_card < 13:
        suit = 0
    elif face_up_card < 26:
        suit = 1
    elif face_up_card < 39:
        suit = 2
    else:
        suit = 3
#A move is a quadruple (player_num, face_up_card, suit, number_of_cards)
#returns true if valid, false if not valid
def check_valid():
    move = history[-1]
    if len(history) >= 2:
        prev = history[-2]
        if (prev[1] % 13) == 1 and move[1] != 0 and move[2] != 0:
            print "#0"
            return False
    if len(move) != 4:
        print "#1"
        return False
    elif move[0] != 1:
        print "#2"
        return False
    elif move[1] == 7 or move[1] == 20 or move[1] == 33 or move[1] == 46:
        return True
    elif (move[1] % 13) != (face_up_card % 13):
        if(move[1] == 0 and move[2] == 0 and move[3] == 1):
            return True
        else:
            print "#3"
            return False
    else:
        return True
    #other checks

def update_face():
    move = history[-1]
    face_up_card = move[2]

def player_move():
    display_hand(hand_player)
    print "face up card is " + str(face_up_card)
    history.append(input_to_tuple())
    while not check_valid():
        print "Input was not correct, please enter correct input"
        history.append(input_to_tuple())
    update_face()

def computer_move():
    p_s = # card to play on, suit, computer's hand, history
    p_s = tuple(p_s)
    result = move(p_s)
    if result[0] == -1:  # game ended
        continue_game = False
        winner = 0;

def deck_length(a_player):
    length = 0
    if a_player == 1:
        for n in hand_player:
            length += n
    else:
        for n in hand_computer:
            length += n
    return length

def is_game_over():
    h1 = deck_length(1)
    h2 = deck_length(0)

    if h1 == 0:
        win = 1
        return True
    if n == 0:
        win = 0
        return True
    if len(deck) == 0:
        win = 2
        return True
    else:
        return False



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
    if is_game_over():
        print "gave over"
        if winner == 0:
            print "computer won"
        elif winner == 1:
            print "You won!"
        else:
            print "Deck ran out of cards!"

    if player_turn:
        print history
        player_move()
        #anything else that needs to be done per move

    else:
        computer_move()

#if winner == 0:
#    print "Computer won!"
#else: print "Human won!"

# exit









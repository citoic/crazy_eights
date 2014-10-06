# CS 156 homework 2
# 6 October 2014
# Katharine Brinker and Edward Ciotic

import random

class Node:

    def __init__(self):
        self.parent = None
        self.children = []
        #TODO: insert data that leafs hold
        #TODO: maybe insert a is_leaf field 

        #also should have temp_hand_size variable

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def insert_child(self, child):
        self.children.append(child)

    #TODO: figure out best way to get children


class CrazyEight:

    #initialize blank array[51] to hold stuff later

    @staticmethod
    def move(self, partial_state):
        player_hand_count = 8  # how many cards player has
        computer_hand_count = 8  # how many cards computer has
        move_scores = []  # higher numbers = better to play
        playable_cards = []  # cards that can be played this turn
        played_cards = []  # cards we know about
        possible_deck = []  # cards in opponent's hand or the draw pile

        face_up_card = partial_state[0]  # current face-up card
        suit = partial_state[1]  # current suit
        computer_hand = partial_state[2]  # cards in AI hand
        history = partial_state[3]  # play history
        history = history[1:]  # first one isn't really a play so ignore

        # figure out players' hand sizes
        for entry in history:
            played_cards.append(entry[2])  # add all played cards to list of cards seen
            if entry[0] == 0:  # computer
                if entry[3] != 0:   # player picked up cards
                    computer_hand_count += entry[3]
                else: computer_hand_count = computer_hand_count - 1
            else:  # human plyer
                if entry[3] != 0:   # player picked up cards
                    player_hand_count += entry[3]
                else: player_hand_count = player_hand_count - 1

        # now you know how many cards each player has

        # make list of playable cards
        for card in computer_hand:
            if can_play(face_up_card, card):
                playable_cards.append(card)

        # now you have a list of playable cards

        # figure out your move
        if len(playable_cards) == 1:  # only one card you can play
            return tuple(0, playable_cards[0], suit(playable_cards[0]), 0)
        elif len(playable_cards) == 0:  # no playable cards
            return tuple(0, face_up_card, suit, 1)  # don't play any cards; draw one
        else:  # more than one playable card
            for i in range(0, 52):
                if not (i in played_cards or i in computer_hand):
                    possible_deck.append(i)
            for j in range(0, 100):
                new_deck = random.shuffle(possible_deck)
                player_hand = []
                for i in range(0, player_hand_count):
                    player_hand.append(new_deck.pop())
                state = tuple(new_deck, player_hand, partial_state)
                good_card = move_perfect_knowledge(state)
                move_scores[good_card] = move_scores[good_card] + 1

        most_votes = max(move_scores)  # highest chance of success
        card_to_play = move_scores.index(most_votes)  # statistically the best card to play

        result = tuple(0, card_to_play, suit(card_to_play), 0)

        return result

        
    @staticmethod
    def move_perfect_knowledge(self, state):
        # new node Head
        # every node has temp_hand_size var. initialize this to actual AI hand size
        # for every playable card in hand, add a new child node to Head with that card's value and temp_hand_size--
        # for each of these new nodes
            # add all of opponent's playable cards as child nodes to your card
            # else, while nothing in opponent's hand is playable, opponent draws. plays first possible card.
                # add that card as a child node
            # if playing any of the opponent's cards reduces opponent's hand to zero, sets temp_hand_size to like 200
            # for each of these opponent moves
                # for every playable  card in (AI) hand, add a new child node to opponent's move with that card's value
                # no playable cards? draw until you get one, increasing temp_hand_size. finally play a card.
                # temp_hand_size --
                #if temp_hand_size == =, set it to like -100 or something.

            # -------- repeat these steps until whatever depth ----------

        #run minimax and a/B pruning to pass temp_hand_size values up to head, keeping smallest one
        # if card with number N gave smallest resulting hand
            # array[N] ++
        

       # return 0  #return the card of choice


# method for checking if a card played is a special card so you can
# simulate special actions



    def can_play(self, face_up, card):
        if card % 13 == 7:  # card is an eight
            return True
        elif card % 13 == face_up % 13:  # same number
            return True
        elif suit(card) == suit(face_up):
                return True
        else return False

    def suit(self, card):
        if card <= 12:
            return 0
        elif card <= 25:
            return 1
        elif card <= 38:
            return 2
        else: return 3

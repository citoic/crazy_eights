# CS 156 homework 2
# 6 October 2014
# Katharine Brinker and Edward Ciotic

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
        #count ones in hand. if only one: play that one card if you can. hand size = 0. you win.
        #else while no playable cards, draw until you get something you can play. play that.
        #otherwise, fill array[51] with all 0s.
        #for 0-51, if that number is not in your hand and hasn't been played, add to list
        #for 1-100:
            # make a permutation of that list. 
            # first numOfCardsInHumansHand are the opponent's hand. rest are face-down cards
            # call move_perfect_knowledge assuming this is the card distribution
        # now that array[51] has been updated, find the biggest number. this is the card you will play.
        # tie? pick the first one
        # play selected card
        # if all your cards are gone, you win
        # else other player's turnnow

        # partial_state = (face_up_card, suit, hand_computer, history)
        # state = (deck, hand_player, partial_state)

        player_hand_count = 8
        computer_hand_count = 8
        possible_moves = []
        playable_cards = []
        played_cards = []

        face_up_card = partial_state[0]
        suit = partial_state[1]
        computer_hand = partial_state[2]
        history = partial_state[3]

        history = history[1:]


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

        for card in computer_hand:
            if can_play(face_up_card, card):
                playable_cards.append(card)

        # now you have a list of playable cards

        if len(playable_cards) == 1:  # only one card you can play
            return tuple(-1, playable_cards[0], suit(playable_cards[0]), 0)
        elif len(playable_cards) == 0:  # no playable cards
            return tuple(0, face_up_card, suit, 1)  # don't play any cards; draw one
        else:  # more than one playable card
            for i in range(0,52):



        return 0 # actually, return a move
        
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
        

        return 0  #actually, return a move


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

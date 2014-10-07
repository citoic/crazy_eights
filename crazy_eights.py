# CS 156 homework 2
# 6 October 2014
# Katharine Brinker and Edward Ciotic

import random, copy

class Node:

    def __init__(self):
        self.parent = None
        self.children = []
        self.card_number = -1  # the card played
        self.player = -1  # which player's move this is
        self.hand_size = -1  # hand size after this play
        self.alpha = 0
        self.beta = 0

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
        head = Node()
        head.player = 0
        deck = state[0]
        player_hand = state[1]
        partial_state = state[2]
        face_up_card = partial_state[0]  # current face-up card
        suit = partial_state[1]  # current suit
        computer_hand = partial_state[2]  # cards in AI hand
        playable_cards = []

        # make list of playable cards
        for card in computer_hand:
            if can_play(face_up_card, card):
                playable_cards.append(card)

        # add child nodes for each possible play
        for i in (0, len(playable_cards)):
            n = Node()
            n.parent = head
            n.card_number = playable_cards[i]
            n.hand_size = len(computer_hand) - 1
            n.player = 0  # computer played this card
            head.children.append(n)

        # simulate opponent's move
        for n in head.children:
            temp_computer_hand = copy.deepcopy(computer_hand)
            temp_player_hand = copy.deepcopy(player_hand)
            temp_computer_hand.pop(temp_computer_hand.index(n.card_number))
            played = False

            for card in temp_player_hand:
                if can_play(n.card_number, card):
                    cn = Node()
                    cn.parent = n
                    cn.card_number = card
                    if len(temp_player_hand) == 1:  # this was their only card
                        cn.hand_size = 9001
                    else: cn.hand_size = n.hand_size
                    cn.player = 1  # player played this card
                    n.children.append(cn)
                    played = True
            if not played:  # opponent had no cards to play
                temp_player_hand.append(deck.pop())  # draw a card
                cn = Node()
                cn.parent = n
                cn.card_number = n.card_number
                cn.player = 1
                n.children.append(cn)

            # computer's move
            for cn in n.children:
                # new theoretical hands for every branch
                t_c_h = copy.deepcopy(temp_computer_hand) 
                t_p_h = copy.deepcopy(temp_player_hand)
                if cn.card_number == n.card_number:
                    continue
                else: t_p_h.pop(t_p_h.index(cn.card_number))
                played = False

                for card in t_c_h:
                    if can_play(cn.card_number, card):
                        ccn = Node()
                        ccn.parent = cn
                        ccn.card_number = card
                        if len(t_c_h) == 1:  # this was our only card
                            ccn.hand_size = -9001
                        else: ccn.hand_size = cn.hand_size - 1
                        ccn.player = 0  # computer played this card
                        cn.children.append(ccn)
                        played = True
                if not played:  # opponent had no cards to play
                    temp_player_hand.append(deck.pop())  # draw a card
                    ccn = Node()
                    ccn.parent = cn
                    ccn.card_number = cn.card_number
                    ccn.player = 0  # computer played this card
                    ccn.hand_size = cn.hand_size + 1
                    cn.children.append(ccn)


        best_card = minimax(head, -10000, 10000)
        return best_card


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

    def minimax(self, node, aplha, beta):
        if len(node.children) == 0:  # leaf node
            return node.hand_size
        elif node.player == 1:  # human player -- maximizer
            for child in node.children:
                alpha = max(alpha, minimax(child, alpha, beta))
                if beta <= alpa:
                    break
            return alpha
        else:  # computer player
            for child in node.children:
                beta = min(beta, minimax(child, alpha, beta))
                if beta <= alpa:
                    break
            return beta

import random
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = ["C", "D", "H", "S"]

class Session:
    def __init__(self, ID, startTime, startMoney, stopTime, stopMoney):
        self.sessionID = ID
        self.startTime = startTime
        self.startMoney = startMoney
        self.stopTime = stopTime
        self.stopMoney = stopMoney


class Card:

    def __init__(self, suit, rank, value):
        self.suits = suit
        self.ranks = rank
        self.value = value

    def __str__(self):
        return self.ranks + self.suits


class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                if rank == "Ace":
                    value = 11
                elif rank == "Jack" or rank == "Queen" or rank == "King":
                    value = 10
                else:
                    value = int(rank)
                self.deck.append(Card(suit, rank, value))

    def deal(self):
        return self.deck.pop(0)

    def shuffle(self):
        random.shuffle(self.deck)

    def count(self):
        return len(self.deck)

    def __str__(self):
        for card in self.deck:
            return(str(card))


class Hand:
    dealer_hand = []
    player_hand = []
    def __init__(self):
        self.hand = []
        self.value = 0

    def add_card(self, card):
        self.hand.append(card)

    def get_card(self):
        for card in self.hand:
            card.ranks + card.suits
        return self.hand


    def count(self):
        for card in self.hand:
            print(len(card))

    def total(self):
        total = 0
        for card in self.hand:
            if card.ranks == "Jack" or card.ranks == "Queen" or card.ranks == "King":
                total += 10
            elif card.ranks == "Ace":
                if total >= 11:
                    total += 1
                else:
                    total += 11
            else:
                total += card.value
        return total

    def __iter__(self):
        self.hand = 1
        return self

    def __next__(self):
        x = self.hand
        self.hand += 1
        return x
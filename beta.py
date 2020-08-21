
import  random
import  itertools
import time


class Deck :
    def __init__ (self, cards: list):
        self.cards = cards

    def is_empty_deck(self):
        return len(self.cards) == 0

    def take_cards(self,num):
        taken_cards =  self.cards[0:num]
        self.cards = self.cards[num:]
        return taken_cards

class Board:
    def __init__(self, cards: list):
        self.cards = cards

    def new_cards (self,cards):
        self.cards += (cards)

    def remove_cards (self,cards):
        for i in cards:
            self.cards.remove(i)

class Card:
    def __init__(self, card_color, card_shape,card_amount,card_filling):
        self.card_color = card_color
        self.card_shape = card_shape
        self.card_amount = card_amount
        self.card_filling = card_filling

    def __repr__(self):
        if self.card_color == 'red':
            return f'{self.card_color}\t\t{self.card_shape}\t{self.card_amount}\t{self.card_filling}'
        else:
            return f'{self.card_color}\t{self.card_shape}\t{self.card_amount}\t{self.card_filling}'

def set_chec(card_1,card_2,card_3,boly):
    if card_1 != card_2 and card_1 != card_3 and card_2 != card_3:
        if len(set([card_1.card_color, card_2.card_color, card_3.card_color])) != 2:
            if len(set([card_1.card_shape, card_2.card_shape, card_3.card_shape])) != 2 :
                if len(set([card_1.card_filling, card_2.card_filling, card_3.card_filling])) != 2:
                    if len(set([card_1.card_amount, card_2.card_amount, card_3.card_amount])) != 2:
                        if boly:
                            print(f'{card_1}\n{card_2}\n{card_3}\n\n\n')
                        return  True
    return False


class Game:
    def __init__(self):
        self.player_point = 0
        self.computer_point = 0

        cards = []
        color = ['r', 'p', 'g']
        shape = ['o', 'd', 's']
        amount = ['1', '2', '3']
        filling = ['so', 'st', 'ou']
        for card in itertools.product(color, shape, amount, filling):
            cards += [Card(*card)]
            random.shuffle(cards)
            self.deck = Deck(cards)

        self.board = Board(self.deck.take_cards(12))

    def play(self):
        exit_loop = False
        while (not self.deck.is_empty_deck() or not exit_loop):
            exit_loop = True
            for set_card in itertools.combinations(self.board.cards, 3):
                if set_chec(*set_card, False):
                    exit_loop = False
                    computer_set = set_card
                    break
            if exit_loop:
                self.board.new_cards(self.deck.take_cards(3))
                continue

            bolyy,player_set = False, None
            time.sleep(2)
            if bolyy:
                if set_chec(*player_set, True):
                    self.player_point += 1
                    print(player_set)
                    self.board.remove_cards(player_set)
                    self.board.new_cards(self.deck.take_cards(3))
                else:
                    self.player_point -= 1
                    print('Mistake')

            else:
                print(computer_set)
                self.board.remove_cards(computer_set)
                self.board.new_cards(self.deck.take_cards(3))
                self.computer_point += 1

        for i in self.board.cards:
            print(f'{i}\n')
        print(self.computer_point)



if __name__ == '__main__':
    game = Game()
    game.play()
    print('git')


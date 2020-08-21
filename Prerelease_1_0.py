
import  random
import  itertools
import time
import tkinter as tk
from PIL import Image, ImageTk

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

    def smart_remove (self,cards):
        old_index = []
        for i in cards:
            old_index += [self.cards.index(i)]
        for i in cards:
            self.cards.remove(i)
        return sorted(old_index)

    def smart_new_cards (self,cards,new_index):
        for card,index in zip(cards,new_index):
            self.cards.insert(index,card)
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
            random.shuffle(cards)
            random.shuffle(cards)
            random.shuffle(cards)
            random.shuffle(cards)

            self.deck = Deck(cards)

        self.board = Board(self.deck.take_cards(12))

    def set_exists(self):

        for set_card in itertools.combinations(self.board.cards, 3):
            if set_chec(*set_card, False):
                return set_card
        return None
    def does_game_end(self):
        if self.deck.is_empty_deck():
            if self.player_point > self.computer_point:
                print('winner winner chiken dinner')
                self.who_won = 'you won'
            elif game.player_point == game.computer_point:
                print('tay')
                self.who_won = 'tay'
            else:
                print('you los')
                self.who_won = 'you lost'
            return (self.who_won)
        else:
            self.board.new_cards(self.deck.take_cards(3))
            return (None)

    def random_time(self):
        x = 1
        y = 3
        return random.randrange(10_000 * x,10_000 * y)

class Gui (tk.Frame):
    def __init__(self, game:Game , master=None):
        tk.Frame.__init__(self, master)
        self.card_button = {}
        self.pack()
        self.pack(fill=tk.BOTH, expand=1)
        self.g_bord = []
        self.game = game
        self.createWidgets(game.board)
        self.after_id = self.after(self.game.random_time(),self.onUpdate)
        self.cards_chosen = []

    def resest_set(self):
        for cardy in self.cards_chosen:
            button = self.card_button[cardy]
            button.config(bg='white')
            button.update()
        self.cards_chosen = []
    def present_winner(self,who_wan):
        label = tk.Label(text=f'{who_wan}')
        label.place(x=180, y=230)
    def createWidgets(self,board:Board):
        button = tk.Button(self,text = 'cancel' , fg="red",
                            command = self.resest_set,)
        button.place(x=180, y=250)
        label = tk.Label(text=f"player points: {self.game.player_point}\t \t \t \t \tcomputer point: {self.game.computer_point}")
        label.place(x= 0, y= 0)
        for img in self.g_bord:
            img.place_forget()
        self.g_bord = []
        x = 0
        y = 20
        for card in board.cards:
            card:Card = card
            load = Image.open(f"C:\\Users\\yishy\\Pictures\\set_card"
                            f"\\{str(card.card_color)[0]}{str(card.card_shape)[0]}"
                              f"{str(card.card_amount)[0]}{str(card.card_filling)[:2]}.png")
            render = ImageTk.PhotoImage(load)
            img = tk.Label(self, image=render)
            img.image = render
            button = tk.Button(self, image = render, fg="red",
                                     bd = 5,)
            button.config(command = lambda card = card, buttenn = button : self.card_chosen(card,buttenn))
            self.card_button[card] = button


            button.place(x=x, y=y)
            if x > 240:
                x = 0
                y += 70
            else:
                x += 110
            self.g_bord += [button]

    def onUpdate(self):
        self.cards_chosen = []
        com_set = self.game.set_exists()
        if com_set is None:
            winner = self.game.does_game_end()
            if winner is not None:
                self.present_winner(winner)
                return None
        else:
            self.com_play(com_set)
        self.createWidgets(self.game.board)
        self.after_id = self.after(self.game.random_time(), self.onUpdate)

    def com_play(self,com_set):
        for cardy in com_set:
            button = self.card_button[cardy]
            button.config(bg='red')
            button.update()
        self.after(3000)
        self.game.computer_point += 1
        old_index = self.game.board.smart_remove(com_set)
        self.game.board.smart_new_cards(self.game.deck.take_cards(3), old_index)

    def card_chosen(self,card,button):
        button.config(bg='green')
        button.update()
        if len(self.cards_chosen) == 3:
            self.cards_chosen = []
        print(card)
        self.cards_chosen += [card]
        if len(self.cards_chosen) == 3:
            self.after(500)
            if set_chec(*self.cards_chosen,True):
                self.game.player_point += 1
                old_index = self.game.board.smart_remove(self.cards_chosen)
                self.game.board.smart_new_cards(self.game.deck.take_cards(3),old_index)
                print('set')
                self.createWidgets(self.game.board)
                self.after_cancel(self.after_id)
                self.after_id = self.after(self.game.random_time(), self.onUpdate)
            else:
                print('not set')
                for cardy in self.cards_chosen:
                    button = self.card_button[cardy]
                    button.config(bg='red')
                    button.update()
                self.after(500)
                for cardy in self.cards_chosen:
                    button = self.card_button[cardy]
                    button.config(bg= 'white')
                    button.update()
                self.game.player_point -= 1
                self.createWidgets(self.game.board)
        print(self.game.player_point)



game = Game()

grafic_boaerd = tk.Tk()
app = Gui(game, master=grafic_boaerd)
grafic_boaerd.geometry("440x400")
grafic_boaerd.mainloop()


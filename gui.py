import tkinter as tk
from tkinter import ttk

import objects
import db
from datetime import time, datetime
import locale
from objects import Session
db.connect()
def start():
    db.connect()
    db.create_session()
    global money
    money = db.get_last_session()
    db.close()
    return money.stopMoney

class BlackjackFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="20 20 20 20")
        self.pack(fill=tk.BOTH, expand=True)
        self.parent = parent
        money = locale.setlocale(locale.LC_ALL, '')
        if money == 'C' or money.startswith('C/'):
            locale.setlocale(locale.LC_ALL, 'en_US')


        self.bet = tk.DoubleVar()
        self.money = tk.StringVar()

        self.pcards = tk.StringVar()
        self.ppoints = tk.StringVar()
        self.dcards = tk.StringVar()
        self.dpoints = tk.StringVar()
        self.result = tk.StringVar()



        self.initComponents()




    def initComponents(self):
        self.money.set(start())
        self.bet.set('')
        self.pack()
        ttk.Label(self, text="Money:").grid\
            (column=0, row=0, sticky=tk.E)
        ttk.Label(self, text="Bet:").grid \
            (column=0, row=1, sticky=tk.E)
        ttk.Label(self, text="DEALER").grid \
            (column=0, row=2, sticky=tk.E)
        ttk.Label(self, text="Cards:").grid \
            (column=0, row=3, sticky=tk.E)
        ttk.Label(self, text="Points:").grid \
            (column=0, row=4, sticky=tk.E)
        ttk.Label(self, text="YOU").grid \
            (column=0, row=5, sticky=tk.E)
        ttk.Label(self, text="Cards:").grid \
            (column=0, row=6, sticky=tk.E)
        ttk.Label(self, text="Points:").grid \
            (column=0, row=7, sticky=tk.E)
        ttk.Label(self, text="RESULT:").grid \
            (column=0, row=9, sticky=tk.E)

        ttk.Entry(self, width=25, textvariable=self.money, state="readonly").grid\
            (column=1, row=0)
        ttk.Entry(self, width=25, textvariable=self.bet).grid \
            (column=1, row=1)
        ttk.Entry(self, width=25, textvariable=self.dcards, state="readonly").grid \
            (column=1, row=3)
        ttk.Entry(self, width=25, textvariable=self.dpoints, state="readonly").grid \
            (column=1, row=4)
        ttk.Entry(self, width=25, textvariable=self.pcards, state="readonly").grid \
            (column=1, row=6)
        ttk.Entry(self, width=25, textvariable=self.ppoints, state="readonly").grid \
            (column=1, row=7)
        ttk.Entry(self, width=25, textvariable=self.result, state="readonly").grid \
            (column=1, row=9)

        self.makeButtons()

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)




    def makeButtons(self):
        buttonFrame = ttk.Frame(self)
        buttonFrame.grid(column=0, row=10, columnspan=2, sticky=tk.E)
        ttk.Button(buttonFrame, text="Play",
                  command=self.play).grid(column=0, row=0)
        ttk.Button(buttonFrame, text="Exit",
                   command=self.parent.destroy).grid(column=1, row=0)
        buttonFrame = ttk.Frame(self)
        buttonFrame.grid(column=0, row=8, columnspan=2, sticky=tk.E)
        ttk.Button(buttonFrame, text="Hit",
                   command=self.hit).grid(column=0, row=0)
        ttk.Button(buttonFrame, text="Stand",
                   command=self.stand).grid(column=1, row=0)





    def blackjack(self, dealer_hand, player_hand):
        if objects.Hand.total(player_hand) == 21:
            self.result.set('You got a Blackjack!')
            global new_money
            betamt = float(self.bet.get())
            total = float(self.money.get())
            new_money = ((betamt * 1.5) + total)
            self.money.set(new_money)
            self.bet.set('')



        elif objects.Hand.total(dealer_hand) == 21:
            self.result.set("The dealer got a blackjack.")
            self.dcards.set(objects.Hand.get_card(dealer_hand))
            betamt = float(self.bet.get())
            total = float(self.money.get())
            new_money = ((total - betamt))
            self.money.set(new_money)
            self.bet.set('')

    def score(self, dealer_hand, player_hand):
        if objects.Hand.total(player_hand) == 21:
            self.dcards.set(objects.Hand.get_card(dealer_hand))
            self.pcards.set(objects.Hand.get_card(player_hand))
            self.dpoints.set(self.display_resultsd(dealer_hand))
            self.ppoints.set(self.display_results(player_hand))
            self.result.set("Congratulations! You win")
            global new_money
            betamt = float(self.bet.get())
            total = float(self.money.get())
            new_money = ((total + betamt))
            self.money.set(new_money)
            self.bet.set('')


        elif objects.Hand.total(dealer_hand) == 21:
            self.dcards.set(objects.Hand.get_card(dealer_hand))
            self.pcards.set(objects.Hand.get_card(player_hand))
            self.dpoints.set(self.display_resultsd(dealer_hand))
            self.ppoints.set(self.display_results(player_hand))
            self.result.set("Sorry, you lost")
            betamt = float(self.bet.get())
            total = float(self.money.get())
            new_money = ((total - betamt))
            self.money.set(new_money)
            self.bet.set('')


        elif objects.Hand.total(player_hand) > 21:
            self.dcards.set(objects.Hand.get_card(dealer_hand))
            self.pcards.set(objects.Hand.get_card(player_hand))
            self.dpoints.set(self.display_resultsd(dealer_hand))
            self.ppoints.set(self.display_results(player_hand))
            self.result.set("You busted!")
            betamt = float(self.bet.get())
            total = float(self.money.get())
            new_money = ((total - betamt))
            self.money.set(new_money)
            self.bet.set('')


        elif objects.Hand.total(dealer_hand) > 21:
            self.dcards.set(objects.Hand.get_card(dealer_hand))
            self.pcards.set(objects.Hand.get_card(player_hand))
            self.dpoints.set(self.display_resultsd(dealer_hand))
            self.ppoints.set(self.display_results(player_hand))
            self.result.set("Dealer busts!")
            betamt = float(self.bet.get())
            total = float(self.money.get())
            new_money = ((total + betamt))
            self.money.set(new_money)
            self.bet.set('')


        elif objects.Hand.total(player_hand) < objects.Hand.total(dealer_hand):
            self.dcards.set(objects.Hand.get_card(dealer_hand))
            self.pcards.set(objects.Hand.get_card(player_hand))
            self.dpoints.set(self.display_resultsd(dealer_hand))
            self.ppoints.set(self.display_results(player_hand))
            self.result.set("Sorry, you lost")
            betamt = float(self.bet.get())
            total = float(self.money.get())
            new_money = ((total - betamt))
            self.money.set(new_money)
            self.bet.set('')


        elif objects.Hand.total(player_hand) > objects.Hand.total(dealer_hand):
            self.dcards.set(objects.Hand.get_card(dealer_hand))
            self.pcards.set(objects.Hand.get_card(player_hand))
            self.dpoints.set(self.display_resultsd(dealer_hand))
            self.ppoints.set(self.display_results(player_hand))
            self.result.set("Congratulations! You win")
            betamt = float(self.bet.get())
            total = float(self.money.get())
            new_money = ((total + betamt))
            self.money.set(new_money)
            self.bet.set('')


        elif objects.Hand.total(player_hand) == objects.Hand.total(dealer_hand):
            self.dcards.set(objects.Hand.get_card(dealer_hand))
            self.pcards.set(objects.Hand.get_card(player_hand))
            self.dpoints.set(self.display_resultsd(dealer_hand))
            self.ppoints.set(self.display_results(player_hand))
            self.result.set("Push!")
            betamt = float(self.bet.get())
            total = float(self.money.get())
            new_money = ((total))
            self.money.set(new_money)
            self.bet.set('')



    def display_results(self, player_hand):
        return (str(objects.Hand.total(player_hand)))

    def display_resultsd(self, dealer_hand):
        return (str(objects.Hand.total(dealer_hand)))

    def play(self):
        try:
            self.bet.get()
        except:
            self.result.set("Invalid bet amount!")
        if self.bet.get() <= 0:
            self.result.set("Invalid bet amount!")
        elif self.bet.get() > float(self.money.get()):
            self.result.set("Invalid bet amount!")
        else:
            self.result.set('')
            global session
            global deck
            deck = objects.Deck()
            deck.shuffle()
            global dealer_hand
            global player_hand
            dealer_hand = objects.Hand()
            player_hand = objects.Hand()
            objects.Hand.add_card(player_hand, objects.Deck.deal(deck))
            objects.Hand.add_card(player_hand, objects.Deck.deal(deck))
            objects.Hand.add_card(dealer_hand, objects.Deck.deal(deck))
            objects.Hand.total(dealer_hand)
            objects.Hand.total(player_hand)
            self.pcards.set(objects.Hand.get_card(player_hand))
            self.dcards.set(objects.Hand.get_card(dealer_hand))
            self.dpoints.set(self.display_resultsd(dealer_hand))
            self.ppoints.set(self.display_results(player_hand))
            objects.Hand.add_card(dealer_hand, objects.Deck.deal(deck))
            self.blackjack(dealer_hand, player_hand)


    def hit(self):
        objects.Hand.add_card(player_hand, objects.Deck.deal(deck))
        self.pcards.set(objects.Hand.get_card(player_hand))
        self.ppoints.set(self.display_results(player_hand))
        while (objects.Hand.total(dealer_hand)) < 17:
            objects.Hand.add_card(dealer_hand, objects.Deck.deal(deck))
        while (objects.Hand.total(player_hand)) < 21:
            return
        self.dcards.set(objects.Hand.get_card(dealer_hand))
        self.dpoints.set(self.display_resultsd(dealer_hand))
        self.score(dealer_hand, player_hand)


    def stand(self):
        while (objects.Hand.total(dealer_hand)) < 17:
            objects.Hand.add_card(dealer_hand, objects.Deck.deal(deck))
        self.dcards.set(objects.Hand.get_card(dealer_hand))
        self.dpoints.set(self.display_resultsd(dealer_hand))
        self.score(dealer_hand, player_hand)




if __name__ == "__main__":
    global start_time
    start_time = datetime.now()
    start_time = start_time.strftime("%I:%M:%S %p")
    root = tk.Tk()
    root.title("Blackjack")
    BlackjackFrame(root)
    root.mainloop()

stop_time = datetime.now()
stop_time = stop_time.strftime("%I:%M:%S %p")

db.connect()
money = (db.get_last_session())
s=Session(money.sessionID + 1, start_time, money.stopMoney , stop_time, new_money)
db.add_session(s)
db.close()

#Dieses Modul soll eine Übersicht der aktuellen in der Liste eingetragenen Spiele ermöglichen
from random import *
import time
from tkinter import *

class Auswählen(Button):
  def auswählen (self):
    class MyButton (Button):
      def aktion (self):
        f=open("games.txt")
        x=len(f.readlines())
        f.close()
        sequence = [i for i in range(0,x)]
        for _ in range(1):
            selection = choice(sequence)
        f=open("games.txt","r")
        lines=f.readlines()
        label2= Label(rahmen, bd = 2, width = 22,text=lines[selection])
        label2.place(x = 200, y = 100)
    fenster = Tk() 
    fenster.geometry("500x400") 
    fenster.title("Spiele auswählen")
    rahmen = Frame(fenster, relief="ridge", borderwidth=5) 
    rahmen.pack(fill="both", expand = 1)
    label = Label(rahmen, text = "Spielauswahl")
    label.config(font=("Arial", 14, "bold")) 
    label.place(x = 50, y = 10)
    label1 = Label(rahmen, text = "Spielname:") 
    label1.place(x = 100, y = 100) 
    label2 = Label(rahmen, bd = 2, width = 22) 
    label2.place(x = 200, y = 100)
    button = MyButton(rahmen,text="Zufallsgeneriert ein Spiel auswählen!") 
    button["command"] = button.aktion 
    button.place(x = 180, y = 220) 
    fenster.mainloop()



def choose():
    f=open("games.txt")
    x=len(f.readlines())
    print("Ich waehle aus {} Spielen".format(x))
    f.close()
    # prepare a sequence
    sequence = [i for i in range(0,x)]
    print(sequence)
    # make choices from the sequence
    for _ in range(1):
        selection = choice(sequence)
        print(selection)
    f=open("games.txt","r")
    lines=f.readlines()
    print("Das Spiel ist: ")
    time.sleep(3)
    print(lines[selection])
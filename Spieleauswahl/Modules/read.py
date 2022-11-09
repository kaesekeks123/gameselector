from tkinter import *


class Anzeigen(Button):
    def anzeigen(self):
        fenster = Tk() 
        fenster.geometry("500x400") 
        fenster.title("Spiele anzeigen")
        rahmen = Frame(fenster, relief="ridge", borderwidth=5) 
        rahmen.pack(fill="both", expand = 1)
        label = Label(rahmen, text = "Die aktuellen Spiele:") 
        label.config(font=("Arial", 14, "bold")) 
        label.pack(pady = 20)
        rahmen2 = Frame(rahmen, relief="ridge", borderwidth=1) 
        rahmen2.pack(pady = 20, padx = 30) 
        f = open("games.txt",'r') 
        inhalt = f.readlines() 
        scrollbar = Scrollbar(rahmen2)
        liste = Listbox(rahmen2, yscrollcommand = scrollbar.set, width = 50) 
        for zeile in inhalt:
                liste.insert(END,zeile)
        f.close() 
        scrollbar.config(command=liste.yview) 
        liste.pack(side="left", fill = "both") 
        scrollbar.pack(side = "left", fill = "y")
        button = Button(rahmen,text="OK", command=fenster.destroy, width = 10, height = 2)
        button.config(font=("Arial", 10)) 
        button.pack(pady = 10) 
        fenster.mainloop()
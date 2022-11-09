from tkinter import *
from Modules.delete import Loeschen 
from Modules.read import * 
from Modules.add import * 
from Modules.overview import * 
from Modules.delete import *

def main():
    y=True

fenster = Tk()
fenster.geometry("700x350")
fenster.title("Main Menu")
rahmen = Frame(fenster, relief="ridge", borderwidth=5) 
rahmen.pack(fill="both", expand = 1)

button1 = Anzeigen(rahmen,text="Display List of Games", width = 20, height = 5) 
button1.config(font=("Arial", 12, "bold")) 
button1.place(x = 50, y = 50)
button1["command"] = button1.anzeigen

button2 = Hinzufuegen(rahmen,text="Add a game", width = 20, height = 5)
button2.config(font=("Arial", 12, "bold")) 
button2.place(x = 430, y = 50)
button2["command"] = button2.hinzufuegen

button3 = Loeschen(rahmen,text="Delete a game", width = 20, height = 5) 
button3.config(font=("Arial", 12, "bold")) 
button3.place(x = 50, y=200)
button3["command"] = button3.loeschen

button4 = Auswählen(rahmen,text="Randomly choose a game", width = 20, height = 5) 
button4.config(font=("Arial", 12, "bold"))
button4.place(x = 430,y = 200) 
button4["command"] = button4.auswählen

label=Label(rahmen,text="GameDay!") #rahmen steht im label, damit die Schrift innerhalb des Rahmens steht
label.place(x=315, y=165) #label einbauen

fenster.mainloop()

if __name__=="__main__":
    main()
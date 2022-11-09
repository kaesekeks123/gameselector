from tkinter import * 

class Hinzufuegen(Button):
  def hinzufuegen(self):
    class MyButton(Button):
      def aktion1 (self):
        f = open("games.txt","a")
        inhalt = eingabe1.get() 
        f.write("\n"+inhalt)
        f.close() 
        fenster.destroy()
    fenster = Tk()
    fenster.geometry("550x400") 
    fenster.title("Spieleauswahl - Adrian, Maxim und Lukas")
    rahmen = Frame(fenster, relief="ridge", borderwidth=5) 
    rahmen.pack(fill="both", expand = 1)
    labelHaupt = Label(rahmen, text = "Welches Spiel möchten Sie hinzufügen?")
    labelHaupt.config(font=("Arial", 14, "bold")) 
    labelHaupt.place(x = 50, y = 10)
    label1 = Label(rahmen, text = "Spiel:") 
    label1.place(x = 100, y = 100) 
    eingabe1 = Entry(rahmen, bd = 2, width = 22) 
    eingabe1.place(x = 200, y = 100)
    button = MyButton(rahmen,text="Eingabe") 
    button["command"] = button.aktion1 
    button.place(x = 180, y = 320) 
    fenster.mainloop()
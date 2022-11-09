from tkinter import * 

class Loeschen(Button):
  def loeschen (self):
    class MyButton (Button):
      def aktion (self):
        spielname = eingabe1.get()
        f = open("games.txt",'r') 
        liste = f.readlines() 
        f.close() 
        geloescht = False 
        for i in range(len(liste)):
          if liste[i] == spielname+"\n":
            f = open("games.txt",'w')
            liste = liste[:i] 
            for linie in liste:
                f.write(linie)
            geloescht = True 
            break
        f.close()
        with open("games.txt") as filehandle:
            lines = filehandle.readlines()
        with open("games.txt", 'w') as filehandle:
            lines = filter(lambda x: x.strip(), lines)
            filehandle.writelines(lines) 
        fenster.destroy() 
        if geloescht:
          fenster2 = Tk()
          fenster2.geometry("300x100") 
          fenster2.title("Spiel gelöscht")
          rahmen2 = Frame(fenster2, relief="ridge", borderwidth=5) 
          rahmen2.pack(fill="both", expand = 1)
          label2 = Label(rahmen2, text="Spiel wurde entfernt") 
          label2.pack(expand = 1)
          button2 = Button(rahmen2,text="OK", command=fenster2.destroy) 
          button2.pack(side = "bottom", pady = 5) 
          fenster2.mainloop()
        else:
          fenster2 = Tk()
          fenster2.geometry("300x100") 
          fenster2.title("Warnung!")
          rahmen2 = Frame(fenster2, relief="ridge", borderwidth=5) 
          rahmen2.pack(fill="both", expand = 1)
          label2 = Label(rahmen2, text="Spiel steht nicht auf der Liste") 
          label2.pack(expand = 1)
          button2 = Button(rahmen2,text="OK", command=fenster2.destroy) 
          button2.pack(side = "bottom", pady = 5) 
          fenster2.mainloop()
    fenster = Tk() 
    fenster.geometry("500x400") 
    fenster.title("Spiele löschen")
    rahmen = Frame(fenster, relief="ridge", borderwidth=5) 
    rahmen.pack(fill="both", expand = 1)
    label = Label(rahmen, text = "Welches Spiel möchten Sie löschen?")
    label.config(font=("Arial", 14, "bold")) 
    label.place(x = 50, y = 10)
    label1 = Label(rahmen, text = "Spielname:") 
    label1.place(x = 100, y = 100) 
    eingabe1 = Entry(rahmen, bd = 2, width = 22) 
    eingabe1.place(x = 200, y = 100)
    button = MyButton(rahmen,text="Eingabe") 
    button["command"] = button.aktion 
    button.place(x = 180, y = 220) 
    fenster.mainloop()
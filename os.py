from tkinter import *
import sys
import os
import random
#module = end

#config = yes
root = Tk()
root.title("Un petit logiciel")
# config = end

#fonction
go = "Bonjour, je suis ton ami (ton PC) !"

def bonjour():
    print(go)

#Les éléments d'affichage
bouton = Button(text="Clique ici !", command=bonjour)
bouton.pack()
#affichage
root.mainloop()
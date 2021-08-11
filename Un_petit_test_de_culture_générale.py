#!/usr/bin/env python3

import sys
import os



HERE = os.path.dirname(sys.argv[0])
sys.path.insert(0, HERE)
os.chdir(HERE)

"""
Le vrai code commence ici !
"""
from tkinter import *
from tkinter import Tk, Label, Frame


root = Tk()
root.title("Un test de culture générale.   Attention les question sont complexes !           Version 0.1")
root.geometry("500x400")
root.config(bg='White')
#Une icone
root.iconbitmap('iconTCG2.ico')


#A
def key_pressed1(event):
    label_w.config(text="1. Qui a construit le pont de pierre(à Bordeaux) et quand !!?? ")


#B
def key_pressed2(event):
    label_w.config(text="2. Qui était le premier ministre de François Mittérand ??")


#C
def key_pressed3(event):
    label_w.config(text="3. Qui était le capitaine du XV de France en 1999 ?")

#D
def key_pressed4(event):
    label_w.config(text="4. Quand est né Emanuel Macron ?")

#E
def key_pressed5(event):
    label_w.config(text="5. Combien d'épreuves les Français ont remportés aux J-O ???")

#F
def key_pressed6(event):
    label_w.config(text="6. Combien d'années peut éspérer vivre un papillion ?")


def key_pressed7(event):
    label_w.config(text="7. Combien de marée y a t'il en 1 an ?")


def key_pressed8(event):
    label_w.config(text="8. Quand est née Brigite Macron ??")

#Les fonctions correction
def qc1(event):
    label_w.config(text="C'est Napoléon 1 qui a construit l'édifice entre 1810 et 1822 !")

#le fonctionnement des raccourcis

root.bind("<A>", key_pressed1)
root.bind("<a>", key_pressed1)

root.bind("<B>", key_pressed2)
root.bind("<b>", key_pressed2)

root.bind("<C>", key_pressed3)
root.bind("<c>", key_pressed3)

root.bind("<D>", key_pressed4)
root.bind("<d>", key_pressed4)

root.bind("<E>", key_pressed5)
root.bind("<e>", key_pressed5)

root.bind("<F>", key_pressed6)
root.bind("<f>", key_pressed6)

root.bind("<G>", key_pressed7)
root.bind("<g>", key_pressed7)

root.bind("<H>", key_pressed8)
root.bind("<h> ", key_pressed8)

#les raccourcis correction
root.bind("<A>", qc1)


# frame principale
frame = Frame(root, bg='White')

# sous boite(frame)
right_frame = Frame(frame, bg='White')

second_frame = Frame(frame, bg='White')

# Un titre
label_title = Label(right_frame , text="Bonjour, bienvenue sur ce quiz de Culture Générale !!   ", font=("Book Antiqua", 20), bg='White', fg='Black')
label_title.pack()

#Un second titre
label_title = Label(second_frame , text="Pour jouer il faut utiliser les lettres(a,b,c,d,e,f,g,h) La correction s'effectue en utilisant les lettre(A,B,C,D,E,F,G,H)en verrouillant la majuscule !!", font='Arial', bg='White', fg='Black')
label_title.pack()

# affichage de la frame pricipale
frame.pack(expand=YES)

#sous boite à droite de la frame principale
right_frame.grid(row=0, column=1, sticky=W)

second_frame.grid(row=1, column=1, sticky=S)








label_w = Label(text="")
label_w.place(x=100, y=100)
label_w.config(bg='White')

root.mainloop()



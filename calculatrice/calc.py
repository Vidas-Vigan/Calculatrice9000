from tkinter import *
from tkinter import messagebox

# Tableaux
fenetre =Tk()
Canvas(fenetre, width=600, height=50, bg='blue').pack(side=TOP ,padx=5,pady=5)
fenetre.geometry("600x600")
fenetre.title("Calculatrice")


# DEFINITIONS DES FONCTIONS
def bouton():
    return(0)

# Horizontal
bouton1 = Button(fenetre, text="1", fg="white", command = bouton)

bouton2 = Button(fenetre, text="2", fg="white", command = bouton)

bouton3 = Button(fenetre, text="3", fg="white", command = bouton)

bouton4 = Button(fenetre, text="4",  fg="white", command = bouton)

bouton5 = Button(fenetre, text="5", fg="white",   command = bouton)

bouton6 = Button(fenetre, text="6", fg="white",  command = bouton)

bouton7 = Button(fenetre, text="7", fg="white", command = bouton  )

# Vertical

# fermeture
bouton1.pack(fill=Y, ipady=20, padx=10, pady=10,)

bouton2.pack(fill=Y, ipady=20, padx=10, pady=10)

bouton3.pack(fill=Y, ipady=20, padx=10, pady=10)

bouton4.pack(fill=Y, ipady=20, padx=10, pady=10)

bouton5.pack(fill=Y, ipady=20, padx=10, pady=10)

bouton6.pack(fill=Y, ipady=20, padx=10, pady=10)

bouton7.pack(fill=Y, ipady=20, padx=10, pady=10)




# Fermeture de tkinter
fenetre.mainloop()




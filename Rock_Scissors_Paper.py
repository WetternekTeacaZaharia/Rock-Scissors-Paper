from tkinter import *
from PIL import Image,ImageTk
from random import randint, choices

#main fereastra
root= Tk()
root.title("Rock Scissors Paper")                                   #titlu fereastra
root.configure(background= "purple")                                #schimb culoarea background-ului(pt mov cod #9b59b6)

#pentru poze (instalare pip in terminal)
piatra_img = ImageTk.PhotoImage(Image.open("piatra.png"))
hartie_img = ImageTk.PhotoImage(Image.open("hartie.png"))
foarfeca_img = ImageTk.PhotoImage(Image.open("foarfeca.png"))

#poze prima perspectiva(mai un set de 3 poze pt perspectiva2)
piatra_img_comp = ImageTk.PhotoImage(Image.open("piatra_2.png"))
hartie_img_comp = ImageTk.PhotoImage(Image.open("hartie_2.png"))
foarfeca_img_comp = ImageTk.PhotoImage(Image.open("foarfeca_2.png"))

#inseram pozele
user_label = Label(root, image = piatra_img,bg="purple")                #bg pt fundal mov
computer_label = Label(root, image = piatra_img_comp,bg="purple")
computer_label.grid(row=1 , column=0)                                   #punem pozele in fereastra(piatra_2.png in stanga)
user_label.grid(row=1, column =4)                                       #piatra.png in dreapta

#pentru scor
jucatorScor = Label(root,text =0, font =100,bg="purple", fg="white")
computerScor = Label(root, text=0,font =100,bg="purple", fg="white" )
computerScor.grid(row=1,column=1)
jucatorScor.grid(row=1,column=3)

#indicatori de nume
user_indicator = Label(root, font=50, text ="EU",bg="purple", fg="white")
computer_indicator = Label(root, font=50, text="COMPUTER",bg="purple", fg="white")
user_indicator.grid(row=0 , column=3 )
computer_indicator.grid(row=0 , column=1 )

#mesajele
mesaje = Label(root,font =50, bg="purple", fg="white")                     #, text = "Ai pierdut!")
mesaje.grid(row=3, column=2)

#actualizarea mesajului
def actualiz_Mesaj(x):
    mesaje ['text'] = x

#actualizarea scorului meu

def actualiz_Iscor():                                                       #scorul jucatorului
     scor = int(jucatorScor["text"])
     scor = scor+ 1
     jucatorScor["text"] = str(scor)

#actualizarea scorului computerului

def actualiz_Cscor():                                                        #scorul computerului
    scor = int(computerScor["text"])
    scor = scor + 1
    computerScor["text"] = str(scor)

#verificam castigatorul

def verif_castigator(jucator, computer):
    if jucator == computer:
        actualiz_Mesaj("Este egalitate!")
    elif jucator == "piatra":
        if computer == "hartie":
            actualiz_Mesaj("Ai pierdut!")
            actualiz_Cscor()
        else:
            actualiz_Mesaj("Ai castigat!")
            actualiz_Iscor()
    elif jucator == "hartie":
        if computer =="foarfeca":
            actualiz_Mesaj("Ai pierdut!")
            actualiz_Cscor()
        else:
            actualiz_Mesaj("Ai castigat!")
            actualiz_Iscor()
    elif jucator == "foarfeca":
        if computer == "piatra":
            actualiz_Mesaj("Ai pierdut!")
            actualiz_Cscor()
        else:
            actualiz_Mesaj("Ai castigat!")
            actualiz_Iscor()
    else:
        pass                                                        # nu vrem sa facem nimic


#alegerea random a computerului,generare random, lista

alegere = ["piatra","hartie","foarfeca"]

def realege(x):

#realegerea unei optiuni a computerului

    computer = alegere[randint(0, 2)]
    if computer == "piatra":
        computer_label.configure(image=piatra_img_comp)
    elif computer == "hartie":
        computer_label.configure(image=hartie_img_comp)
    else:
        computer_label.configure(image = foarfeca_img_comp)
#
#realegerea unei optiuni pt jucator 1
    if x=="piatra":
        user_label.configure(image=piatra_img)
    elif x=="hartie":
        user_label.configure(image=hartie_img)
    else:
        user_label.configure(image=foarfeca_img)
    verif_castigator(x,computer)

#butoane de selectare
piatra = Button(root,width=20, height=2, text="PIATRA", bg="orange", fg="white",command = lambda:realege("piatra"))
hartie = Button(root,width=20, height=2, text="HARTIE", bg="green", fg="white",command = lambda:realege("hartie"))
foarfeca = Button(root,width=20, height=2, text="FOARFECA", bg="blue", fg="white",command = lambda:realege("foarfeca"))
piatra.grid(row=2,column=1)
hartie.grid(row=2,column=2)
foarfeca.grid(row=2,column=3)


#mentinere interfata grafica deschisa
root.mainloop()
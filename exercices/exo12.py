from random import randint
word=""
word=input("Veuillez introduire un mot \n")
while word != "quit":
    if word=="dice":
        y=randint(1,6)
        print(y)
    elif word=="sum":
        somme=0
        for i in range (1,101):
            somme= somme + i
        print(somme)
    elif word=="password":
        x=randint(10,15)
        for i in range (x):
            z=randint(0,9)
            print(z,end="")
        print()
    else:
        print("Vous n'avez pas compris.Veuillez réssayer.")
    word=input("Veuillez introduire un mot \n")
from random import randint
x=" "
while True:
    x=input("Voulez-vous lancer le dé:oui/non")
    if x=="oui":
        y=randint(1,6)
        print(y)
    else:
        break

    
    

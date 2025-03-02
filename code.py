import random
from art import logo
print(logo)

list1=[11,2,3,4,5,6,7,8,9,10,10,10,10]

while True:
    b=0
    c=0
    ask=input("Do you want to play the BlackJack Game? type 'y' or 'n': ")

    if ask=="y":
        iam=[]
        iam=random.sample(list1,k=2)
        print("Your Cards: "+str(iam),", Current score: "+str(iam[0]+iam[1]))

        #computer's choice
        comp=[]
        comp=random.sample(list1,k=2)
        print("Computer's first card: "+str(comp[0]))

        check=True

        typen=input("Type 'y' to get another card, type 'n' to pass: ")
        while check:
            if typen=="y":
                iam+=(random.sample(list1,k=1))
                print("Your cards: "+str(iam))
                print("Computer's first card: "+str(comp[0]))
                typen=input("Type 'y' to get another card, type 'n' to pass: ")

                #computer's choice
                a=['True','False']
                if random.choice(a)=='True':
                    comp+=random.sample(list1,k=1)
                    print(comp)
                else:
                    print("Computer's first card: "+str(comp[0]))

            elif typen=="n":
                check=False

                #computer's choice
                a=['True','False']
                if random.choice(a)=='True':
                    comp+=random.sample(list1,k=1)

                for i in iam:
                    b+=i
                print("Your final hand: "+str(iam) +",final score: "+str(b))
                for j in comp:
                    c+=j
                print("Computer's final hand: "+str(comp)+",final score: "+str(c))
                if (b>21) & ((c<21) or (c==21)):
                    print("You lose!.\nYou are over valued.")
                elif (b==21) & (c==21):
                    print("match draw")
                elif (b==21) & ((c<21) or (c>21)):
                    print("You Win")
                elif (b<21) & (c>21):
                    print("You Win")
                elif (b==c) & (b<21):
                    print("Match Draw")
                elif (b>21) & (c>21):
                    print("You both lose")

    elif ask=="n":
        break
    else:
        print("Invalid input please type 'y' or 'n': ")



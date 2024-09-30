import time
import random

#Spel titel
print("Välkommen till Rock em Sock em")

Spelare1namn =input("Välj din karaktärs namn: ")
Spelare2namn = "John" #Fiendens namn
Spelare1HP = int(60) #HP
Spelare2HP = int(60) #HP

time.sleep(1)

#Announcement
print(f"Idag kommer {Spelare1namn} och {Spelare2namn} slåss till döden!")

time.sleep(1)

print("LETS GET READY TO RUMBLE!!!!!!")

time.sleep(2)

while Spelare1HP > 0 and Spelare2HP > 0:
    if random.choice([True, False]):
        Spelare1HP -= random.randint(3, 15)

    if random.choice([False, True]):
        Spelare2HP -= random.randint(3, 15)
    
    print(f"{Spelare1namn} har {Spelare1HP} HP kvar!")
    print(f"{Spelare2namn} har {Spelare2HP} HP kvar!")

    time.sleep(0.75)

if Spelare1HP >= 0:
    print(f"{Spelare2namn} has been KNOCKED OUT!")
    time.sleep(1)
    print(f"{Spelare1namn} har Vunnit!")

elif Spelare2HP >= 0:
    print(f"{Spelare1namn} has been KNOCKED OUT!")
    time.sleep(1)
    print(f"{Spelare2namn} har vunnit!")

else:
    print("DKO!!!")











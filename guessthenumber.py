###
# välja ett tal
print("Welcome to guess a number")

correctNumber = 6
numOfguesses = 3

# be om en siffra

while (numOfguesses > 0):
    print("Guess a number")
    guess = int(input())
    #print ("you guessed ")
    #print(guess)

    numOfguesses -= 1

    # kolla om siffran är större eller lika

    if (guess > correctNumber):
        print("you guessed to large. Try again.")
        # mindre eller lika§
    elif (guess < correctNumber):
        print("you guessed to low. Try again.")
    else: 
        print (" you guessed correct.")
        numOfguesses = 0


    # göra tre gånger

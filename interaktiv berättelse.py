from time import sleep


failure_ending = "Spela"
success_route = "Plugga"
success_ending1 = "Sova"
success_ending2 = "Plugga vidare"

print ("Vällkommen till läxa eller spel?\n   ") #Spel Titel

sleep (2)

print ("\n Du har 3 timmar kvar innan du behöver läga ner dig för att sova och du har NO prov imorgon. kommer du använda resten av din tid för att plugga för provet eller kommer du spela fortnite")

success_route = success_route.lower()
failure_ending = failure_ending.lower()
success_ending1 = success_ending1.lower()
success_ending2 = success_ending2.lower()

sleep (1)

answer = input("Vad gör du? Spela eller plugga?: \n") #Första Valet

sleep(1)

if (answer == failure_ending):
    print ("Efter att ha haft en intensiv fortnite session inatt, lägger du dig på sängen och sover för natten. Dagen efter misslyckas du hårt med provet och får ett F i kursen")
    sleep (2)
    print ("Failure Ending.")
else: 
    sleep(1)
    (answer == success_route)
    print ("efter 3 timmar inser du att du skulle ha pluggat mycket tidigare. Med kunskapen du har just nu kan du få godkänt men inget mer. Väljer du att ge upp din sömntid för att få ett bättre betyg eller sover du?")
    answer_2 = input ("Vad gör du? Sova eller Plugga vidare?: \n")
    if (answer_2 == success_ending1):
        sleep(3)
        print ("Du vaknar up och går till skolan för att genomföra NO provet. 2 Veckor efter provet får du dina resultat och fick E som betyg")
        print ("Mediocre Ending.")
    else:
        sleep(1)
        if (answer_2 == success_ending2):
            print ("Du vaknar up halv död och förbereder dig inför skolan. Innan du lämnade ditt hem drack du en kopp svart kaffe för att vakna upp. Du genomförde Provet och fick resultatet 2 veckor senare. Du fick B som betyg!")
print("Tack för att du har deltagit i mitt spel:D")
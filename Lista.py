a_list = ["Liv", "Mohammed", "Henrik", "Mikael", "Karim", "Johan"]
#print ("Hello" + a_list[2])

names = ["Eric", "Yunus", "Liam", "Max", "Adrian"]
Colours = ["Purple", "Red", "Blue", "Green", "Orange"]
index = 0 #where we begin

#while (index < names.len(names)):  
#    print (f"{names[index]} has favorite colour {Colours[index]}")
#    index += 1

#for name in names:
#    print("Hello " + name)


#print (f"{names[0]} has favorite colour {Colours[0]}"); #same as print(names[0] + "has favorite colour" {Colours[0]});

dogs = ["Fido", "Spot", "Scooby"]

new_dog = input("what is the name of the new dog? ")

dogs.append(new_dog)

print(f"the dogs currently at daycare are {dogs}")

leaving_dog = input ("Who is leaving the daycare? ")

dogs.remove(leaving_dog)

print(f"{leaving_dog} has left the daycare, only {dogs} are here now.")
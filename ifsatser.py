corrPass = "computers"
corrUser = "Liv"

username = input("username: ")
password = input("password: ")

username= username.lower()


if (username == corrUser):
    print ("correct user: " + corrUser)
    if (password == corrPass): 
        print("correct password: " + corrPass)
    else:
        print("worng password")
else: 
    print ("wrong username:" + username)
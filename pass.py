user = input("Username: ")
pas = input("Password: ")

if user.isalpha() and pas.isalnum():
    print("login successfull")
else:
    print("login failed try again")

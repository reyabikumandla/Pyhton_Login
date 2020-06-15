username = input("Enter Username: ")
password = input("Enter Password: ")
checkvalues = True

if username != "Reya" and \
        password != "Chandra123":
            print("Invalid Login. Please Try again.")
            checkvalues = False

if username != "Reya" and password != "Chandra123":
    print("Wrong Username and Password. Please Try Again.")

if(checkvalues == True):
    if username == "Reya":
        if password == "Chandra123":
            print("Hello", username,".", "You Have Logged In Succussfully!")
        else:
            print("Invalid Password. Please Try Again.")
    else:
        print("Invalid Username. Please Try Again.")



#
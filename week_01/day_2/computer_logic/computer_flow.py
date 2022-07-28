
def power():
    is_powered = input("Is the PC tuned on? ")
    if is_powered == "no":
        print("Turn on the computer!")
        power()
    else:
        boot()

def boot():
    bootup = input("Did the PC boot normally? ")
    if bootup == "no":
        pluggedin = input("Is it plugged in properly? ")
        if pluggedin == "yes":
            print("Computer is broken!")
        else:
        # if pluggedin == "no":
            print("Plug it in and try agian!")
            power()
    else:
        login()

def login():
    pswd = input("Please enter password " )
    if pswd == "password":
        print("Logged in correctly!")
    elif pswd != "password":
        print("WRONG PASSWORD!")
        login()

power()
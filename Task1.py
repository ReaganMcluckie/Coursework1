# REAGAN MCLUCKIE | 07/10/2026 | 30226399 | B01888719
def cliMenu() -> None:
    print("1. Security Event Counter")
    print("2. Brute-Force Simulation")
    print("3. Login Authentication")
    print("4. Exit")

def securityEventCounter() -> None:
    # Makes the password admin123
    correctpassword = "admin123"
    counter = 0

    # loops 10 times asking the user to enter a password and if the user enters the correct password it increases the counter by 1
    for i in range(10):
        userinput = str(input("Please enter the password: "))
        if userinput == correctpassword:
            counter += counter

    counter = 10 - counter

    # Calculates the percentage of unsuccessful attempts and prints a security alert if more than 50% of inputs are wrong
    percentage = (counter / 10) * 100
    if percentage >= 50:
        print("SECURITY ALERT: More than 50% of the attempts were unsuccessful.")


def bruteForceSimulation() -> None:
    # Makes the password admin123
    correctpassword = "admin123"
    attempts = 0

    # keeps asking the user to enter a password until they enter the correct one adding 1 to the attempts counter each try
    while True:
        userinput = str(input("Please enter the password: "))
        attempts += 1
        if userinput == correctpassword:
            print(f"Access granted after {attempts} attempts.")
            break
        else:
            print("Access denied. Please try again.")

def login(username: str, password: str) -> bool:
    # Sets the username and password to admin and admin123
    valid_username = "admin"
    valid_password = "admin123"

    max_attempts = 3

    for i in range(max_attempts):
        # if the username and password match the set username and password it will print that the login was successful and return True
        if username == valid_username and password == valid_password:
            print("Login successful.")
            return True
        else:
            # if the username and password do not match the set username and password it will print that the login failed and ask the user to enter a username and password again
            print(f"Login failed.")
            if i < max_attempts - 1:
                username = str(input("Please enter your username: "))
                password = str(input("Please enter your password: "))
        # This bellow insures that the user only has 3 attemps before the account is frozen
        if i == max_attempts - 1:
            print("This account is frozen for 24 hours.")
            return False

def exitProgram() -> None:
    # allows the user to exit the program
    exit()

def main():
    # displays the interface in the terminal and asks the user to choose one of the options
    cliMenu()
    userinput = int(input("Please Choose an option: "))

    # if the userinput was 1 it will run the securityEventCounter function
    if userinput == 1:
        securityEventCounter()
    # if the userinput was 2 it will run the bruteForceSimulation function
    elif userinput == 2:
        bruteForceSimulation()
    # if the userinput was 3 it will ask the user to enter a username and password then pass those values into the login function and return either True or False
    elif userinput == 3:
        usernameinput = str(input("Please enter your username: "))
        passwordinput = str(input("Please enter your password: "))
        login(usernameinput, passwordinput)
    # if the userinput was 4 it will say thanks for using the security tool and exit the program
    elif userinput == 4:
        print("Thank you for using the security tool.")
        exitProgram()

    
if __name__ == "__main__":
    main()
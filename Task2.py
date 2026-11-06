# REAGAN MCLUCKIE | 30226399 | B01888719

import random
import socket
from datetime import datetime

def generateEventID() -> int:
    return random.randint(1000, 9999)

def generateTimestamp() -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return timestamp

def getIPAddress() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()

    return ip_address

def login(username: str, password: str) -> bool:
    valid_username = "admin"
    valid_password = "admin123"

    if username == valid_username and password == valid_password:
        return True
    else:
        return False

def main():
    userinput = str(input("Please enter your username: "))
    passinput = str(input("Please enter your password: "))

    loginValid = login(userinput, passinput)

    print("SECURITY EVENT LOG")
    print("------------------")

    if loginValid:
        print(f"Event ID: {generateEventID()}")
        print(f"Username: {userinput}")
        print(f"IP Address: {getIPAddress()}")
        print(f"Event: Successful login")
        print(f"Timestamp: {generateTimestamp()}")
    else:
        print(f"Event ID: {generateEventID()}")
        print(f"Username: {userinput}")
        print(f"IP Address: {getIPAddress()}")
        print(f"Event: Failed login")
        print(f"Timestamp: {generateTimestamp()}")

if __name__ == "__main__":
    main()
# REAGAN MCLUCKIE | 30226399 | B01888719

def validate_ip(ip: str) -> bool:
    parts = ip.split(".")
    parts = [part.strip() for part in parts]
    isIpValid = True

    if len(parts) != 4:
        isIpValid = False

    for part in parts:
        if not part.isdigit():
            isIpValid = False

        number = int(part)

        if number < 0 or number > 255:
            isIpValid = False

    return isIpValid

        

def main() -> None:
    try:
        userinput = str(input("Please enter an IP: "))

        isValid = validate_ip(userinput)
    except ValueError:
        print("Invalid IP address")

    if isValid:
        print("Valid IP address")
    else:
        print("Invalid IP address")

if __name__ == "__main__":
    main()
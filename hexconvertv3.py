def convertHexToDec(hexSubString):
    return str(int(hexSubString, 16))


hexaString = ""
while hexaString != "exit":
    hexaString = input("What is the hex?: ")
    if hexaString == "exit":
        quit()
    hexaString.replace(" ", " ")
    outString = ""

    if len(hexaString) % 2 == 0:
        for i in range(0, len(hexaString), 2):
            subStr = hexaString[i] + hexaString[i + 1]
            outString += convertHexToDec(subStr.upper()) + " "
    else:
        print("Odd number of hex chars. Try again.")

    print(f"{outString}")

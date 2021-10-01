def convertHexToDec(hexSubString):
        return chr(int(hexSubString, 16))

hexaString = input("What is the hex?: ")
hexaString.replace(" "," ")
outString = ""

if len(hexaString) % 2 == 0:
    for i in range(0,len(hexaString),2):
        subStr = hexaString[i] + hexaString[i+1]
        outString = convertHexToDec(subStr)
while hexaString != "exit":
    print("Odd number of hex chars. Try again.")
    hexaString = input("What is the hex?: ")

    
    print(outString)

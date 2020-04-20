# asks user for name and number, then counts to that number x 2s
print("\033c")  # clears the console window

MAX_NUM_SIZE = 100  # Change this to allow larger numbers
MAX_NAME_SIZE = 12  # Define longest allowed Name string

def doCount():
    uName, uNum, strOut = '', '', '' # Predefine my variables
    
    # Validate name (not blank and between 3 - predefined upper limit)
    while len(uName) < 3:
        uName = input("Hi, what's your name? (3 or more chars) ")

    uName = uName[:MAX_NAME_SIZE] # Truncate name if too long

    print("Hello " + uName.capitalize())

    # Call function to validate number input
    while checkNum(uNum) == False:
        uNum = input("Please enter an integer, between 3 to %s: " % (MAX_NUM_SIZE))

    print("You entered: " + str(uNum))

    # Detect if number is even or odd
    if int(uNum) % 2 == 0: #even
        startNum = 0
    else: #odd
        startNum = 1

    # Count by 2s, starting at 0 or 1
    for i in range(startNum, int(uNum)+1, 2):
        # construct my output on one line before printingbetween 
        strOut += str(i) + " "
    print(strOut)

# Number input validation function
def checkNum(x):
    if str(x).isdigit() == True:  # is it a digit
        x = int(x)
        if x >= 3 and x <= MAX_NUM_SIZE:  # Check unmber is in range
            return x
        else:
            print("Number outside of range")
            return False
    else:
        return False

# Run the first function
if __name__ == '__main__':
    doCount()
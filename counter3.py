# asks user for name and number, then counts to that number x 2s
# Count by 2s, starting at 0 (if even) or 1 (if odd)

print("\033c")  # clears the console window (Mac/Linux only?)

MIN_NUM_SIZE = 3
MAX_NUM_SIZE = 100  # Change this to allow larger numbers
MIN_NAME_SIZE = 3   # Define shortest allowed Name string
MAX_NAME_SIZE = 12  # Define longest allowed Name string

uName, uNum, strOut = '', '', '' # Predefine some empty variables

# Number input validation function
def checkNum(x):
    if str(x).isdigit() == True:  # is it a digit
        x = int(x)
        # Check number is in range
        if x >= MIN_NUM_SIZE and x <= MAX_NUM_SIZE:
            return
        else:
            print("Number outside of range")
            return False
    else:
        return False
#end of function checkNum()


# Validate name (not blank and between 3 - predefined upper limit)
while len(uName) < MIN_NAME_SIZE:
    uName = input("Hi, what's your name? (" + str(MIN_NAME_SIZE) + " or more chars) ")

uName = uName[:MAX_NAME_SIZE] # Truncate name if too long

print("Hello " + uName.capitalize())

# Validate number input
while checkNum(uNum) == False:
    uNum = input("Please enter an integer, between " + str(MIN_NUM_SIZE) + " to %s: " % (MAX_NUM_SIZE))

if int(uNum) > MAX_NUM_SIZE:  # this should never happen?  Function checkNum() does not allow
    uNum = MAX_NUM_SIZE
    print('x is now ' + str(uNum))

print("You entered: " + str(uNum))

# Detect if number is even or odd
if int(uNum) % 2 == 0: #even
    startNum = 0
else: #odd
    startNum = 1

# Count by 2s, starting at 0 (if even) or 1 (if odd)
for i in range(startNum, int(uNum)+1, 2):
    # construct my output on one line before printingbetween
    strOut += str(i) + " "
print(strOut)

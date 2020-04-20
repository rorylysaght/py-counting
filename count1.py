# Python3: Ask for number, count by 2s

#currentNumber = 0
# test if countby is a number

myname = input("What is your name? ")
print("Hello " + myname)


while True:
	try:
		countby = int(input("Enter a number "))
	except ValueError:
		print("Sorry, I didn't understand that. Please enter an integer (<= 100)")


	else:
		while countby > 100:
			print("Too big - number should be less than 101")
			countby = int(input("Please enter a number again "))
		print("Your number is " + str(countby))
		break



for x in range(0,countby,2):
    print(x)

#print("You got it!")
print("\033[1;32;40m You got it!  \n")
print("\033[1;37;40m ") # set screen back to normal

	#if countby %2:
	#	print("count by odd")


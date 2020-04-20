# Prog to ask user for name and number, then count by 2's
# Note this is bad code: no validation/sanitization of inputs
# For demonstration only - students must add data input validation/sanitization

print ('####### Counting by 2s #######')

myName = input('Your name? ').capitalize()

print("Hello " + myName)

endNum = input('Enter a number: ')
endNum = int(endNum)  # convert string to integer

input('Counting to ' + str(endNum) + ' - press Enter to start: ')

for x in range(1, endNum+1, 1):
	print (x)

print('Done!')

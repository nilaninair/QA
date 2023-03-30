a = int (input (" Enter the first exam mark "))
b = int (input (" Enter the second exam mark "))
c = int (input (" Enter the third exam mark "))
average = (a+b+c)/3
print ("The average exam mark is ", average)
if average > 65: 
	print ("You have passed")
elif average < 65:
	print ("You have failed")
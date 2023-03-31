a = int (input ("Enter first number "))
b = int (input ("Enter second number "))
c = int (input ("Enter third number "))
print ("Maximum is ", end= '')
if b <= a >= c:
    print (a)
elif a <= b >= c:
    print (b)
elif a <= c >= b:
    print (c)

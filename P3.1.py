# P3.1 Write a program that reads an integer and prints whether it is negative, zero, or positive

# Take the input from user
i=int(input('Plase enter an integer (such as negative, zero or positive) : '))
print ()
if i<0:
    print (i, ' is a negative number.')
elif i>0:
    print (i, 'is a positive number. ')
else:
    print (i, ' ia a zero')

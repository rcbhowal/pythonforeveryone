# Write a program that reads a floating point number and prints 'zero' if the number
# is zero. Otherwise, print 'positive' or negative'. Add 'small' if the absolute value
# value of that number is less than 1, or 'large' if exceeds 1,000,000.

# Take the input from user
x=float(input('Enter a number it could be positive, negative, zero : '))
if x>0:
    print (x,' Is positive number')
    if abs(x)>1000000:
        print ('Large')
if x<0:
    print(x,' Is Negative')
    if abs(x)<1:
        print ('Small')
if x==0:
    print (x,' Is zero')



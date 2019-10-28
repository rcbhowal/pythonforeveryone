#
## Read three number from user
#


# Read the input from user
num1=float(input('Enter 1st number: '))
num2=float(input('Enter 2nd number: '))
num3=float(input('Enter third number: '))

# set the rules or condition
if num1<num2<num3:
    print ('Increasing')
elif num1>num2>num3:
    print ('Decreasing')
else:
    print ('Neither')

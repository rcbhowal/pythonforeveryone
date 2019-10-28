#
## Read three number and ask for strictly or lenient mode for increasing or decreasing
#

# Read the input from user
num1=float(input('Enter 1st number: '))
num2=float(input('Enter 2nd number: '))
num3=float(input('Enter third number: '))

# ask for mode
mode=input('Enter mode ''strict'' or ''lenient'' before you start: ')

# set the rules or condition
if mode=='strict':
    if num1<num2<num3:
        print ('Increasing')
    elif num1>num2>num3:
        print ('Decreasing')
    else:
        print ('Neither')
elif mode=='lenient':
    if num1<=num2<=num3:
        print ('Increasing')
    elif num1>=num2>=num3:
        print ('Decreasing')
    else:
        print ('Neither')
else:
    print ('You did not enter a valid item! try again..')

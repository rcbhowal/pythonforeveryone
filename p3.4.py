# Write a program that reads three numbers and prints 'all the same' if they are all the
# same, 'all different' if they are all different, and 'neither' otherwise.

# Take the input
x=int(input('Enter the first number: '))
y=int(input('Enter the second number: '))
z=int(input('Enter the third number: '))

# set the rules
if x==y==z:
    print ('All the same')
if x!=y!=z:
    print ('All different')
else:
    print ('Neither')

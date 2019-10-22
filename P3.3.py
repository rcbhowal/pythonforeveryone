# Write a progam that reads an integer and prints how may digits the number has, by
# checking whether the number is >=10, >100, and so on. (A ssume that all integers are
# less then ten billions.) if the number is negative, first multiply it by -1.

# Take the input from user
n=int(input('Enter the integer: '))
m=str(n)
print ()
#set the condistion
if n>=10 or n>=100:
    print ('Total digit in it ', len(m))
if n<0:
    print ('The number is negative and multiply by -1 : ', n*-1)
if n>10000000:
    print ('Our of range ! please enter a number less than 10 billion.')
    print ('Thank you try again.')

#
## Translate a letter grade into a number grade.
#


# Read the input

grade=(input('Enter the letter grade A/B/C/D: ')).upper()

# Set the condition

if grade=='A+':
    print ('The numeric value is: 4.0')
elif grade=='A':
    print ('The numeric value is: 3.7')
elif grade== 'B':
    print ('The numeric value is: 3.4')
elif grade=='B-':
    print ('The numeric value is: 3.1')
elif grade=='C':
    print ('The numeric value is 2.8')
elif grade=='C-':
    print ('The numeric value is: 2.5')
elif grade=='D':
    print ('The numeric value is: 2.2')
elif grade=='D-':
    print ('The numeric value is: 1.9')

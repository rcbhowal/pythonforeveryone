#
## Reads a temperature value and the letter C for Celsius or F for Fahrenheit.
## And convert them

# Take the input
print ('Do you use Farenheit (F) or Celcius? (C)')
print ()
degreeUnit=(input('Enter F or C : ')).upper()
temp=int(input('What the temperature of the water?'))
altitude=int(input('Enter a altitude to find the boiling point: '))

# Set the condition if input is F in line with temperature 

if degreeUnit =='F' and temp<=32:
    print ('The water is frozen.')
elif degreeUnit=='F' and temp>=212:
    print ('The water is a gas')
elif degreeUnit=='F' and temp>=33 or temp<=212:
    print ('The water is a liquid.')

# Set the condition if input is C in line with temperature

elif degreeUnit=='C' and temp <=0:
    print ('The water is frozen.')
elif degreeUnit=='C' and temp>=100:
    print ('The water is a gas.')
elif degreeUnit =='C' and temp>=1 or temp<=99:
    print ('The water is a liquid.')
else:
    print ('Please try again, something went wrong.')


#
## Read the three strings and sorts them lexicographically
#

# Read the input from user
string1=str(input('Enter a string: '))
string2=str(input('Enter a string: '))
string3=str(input('Enter a string: '))
print ()
# Order the strings so that first comes before second, which omes before third
if str1<=str2 and str1<=str3:
    first=str1
    if str2<=Str3:
        second=str2
        third=str3
    else:
        second=str3
        third=str2
elif str2<=str1 and str2<=str3:
    first=str2
    if str1<=str2:
        second=str1
        third=str3
    else:
        second=str3
        third=str1
else:
    first=str3
    if str2<str1:
        second=str2
        third=str1

# Display the result
print (first)
print (second)
print (third)


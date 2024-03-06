string=input("Input:")
output=''
for i in string:
    if i.lower() in ('a','e','i','o','u'):
        output=output
    else:
        output += i
print('Output:'+output)
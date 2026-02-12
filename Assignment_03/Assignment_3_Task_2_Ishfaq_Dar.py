import math
print("Enter a number : ")

num = int(input())

if num < 0:
    print("Negative number is not allowed for square root/logrithm")
elif num == 0:
    print("The square root of 0 is 0.0")
    print("The log of 0 is undefined")
    print("The sine of 0 is 0.0")
else:
    sqrt = math.sqrt(num)
    log = math.log(num)
    sine = math.sin(num)
   
    print("The square root of", num, "is", sqrt)
    print("The log of", num, "is", log)
    print("The sine of", num, "is", sine)
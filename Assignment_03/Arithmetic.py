def arithmetic(num1, num2) :
    res1 = num1 + num2
    res2 = num1 - num2  
    res2 = num1 - num2  
    res3 = num1 * num2
    res4 = num1 / num2
    return res1, res2, res3, res4



val1 = int(input("Enter first number: "))
val2 = int(input("Enter second number: "))    

res1,res2,res3,res4 = arithmetic(val1,val2)

print(f"Addition of {val1} and {val2} is :",res1)
print(f"Subtraction of {val1} and {val2} is :",res2)    
print(f"multiplication of {val1} and {val2} is :",res3 )
print(f"Division of {val1} and {val2} is :",res4 )

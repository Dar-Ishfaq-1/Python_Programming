Num = int(input("Enter a number: "))
if Num == 0:
    print("You have entered Zero.")
elif Num < 0:
    print(f"{Num} is a Negative number.")

elif Num % 2 == 0:
    print(f"{Num} is an Even number.")
else: 
    print(f"{Num} is an Odd number.") 

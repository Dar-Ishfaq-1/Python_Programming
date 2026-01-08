
def fact():
  num = int(input("Enter a number to find its factorial: "))
  if num < 0:
    return "Factorial is not defined for negative numbers."
  elif num == 0 or num == 1:
    return 1
  else:
    factorial = 1
    for i in range(2, num + 1):
      factorial *= i
    return print(f'The Factorial of {num} is:', factorial)
#print(fact())

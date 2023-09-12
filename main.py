def fact_rect(n):
  if n==0 or n==1:
    return 1
  else :
    return n*fact_rect(n-1)

number = int(input("Enter a number : "))
res = fact_rect(number)
print("The factorial of {} is {}." .format(number,res))
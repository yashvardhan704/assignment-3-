# factorial of a number
n=int(input("enter a number: "))

def factorial(n):
    if n==0 or n==1:
        return 1
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
answer=factorial(n)
print(f"the factorial of {n} is: {answer}")




def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
        
# n = int(input("enter n:"))
print(factorial(5))
    
    
      
# lets find out fibonacci number
# 
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1)+fibo(n-1-1)
    # fibo(0) == 0
    # fibo(1) == 1
    # fibo(n) = fibo(n-1)
    # return fibo(i)
print(fibo(6))
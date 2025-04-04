# def lambda_func(x):
#     '''
#     in python lambda function is a anonymous function without a name
#     It is defined by using lambda keyword and has the following syntax
#     lambda arguments: expression
#     '''
#     return x*2
# print(lambda_func(5))
# print(lambda_func.__doc__)
lambda2 = lambda x : x * 2
cube = lambda x : x * x * x
avg = lambda c,b:(c+b)/2
# print(eval(5+6))
def function2( value , fx):
    return value + fx(value)
print(lambda2(5))
print(cube(6))
print(avg(5,44))
# print(function2(cube , 6))#we can also write as below line of code
print(function2(6,lambda c:c+c+c))
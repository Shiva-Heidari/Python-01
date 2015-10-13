def fib_loop(n):
    '''
    Returns the nth number in the fibonachi series.
   
    It uses for loop to calculate it.
    '''

    
def fib_recursion(n):
    '''
    Returns the nth number in the fibonachi series.
   
    It uses for loop to calculate it.
    '''
def F(x):
    if x == 0: return 0
    elif x == 1: return 1
    else: 
        return F(x-1)+F(x-2)
def fib_generator(n):
    '''
    Generator version of fibonacci.
    '''

print(fib_loop(8))
print(fib_recursion(13))
print([i for i in fib_generator(14)])

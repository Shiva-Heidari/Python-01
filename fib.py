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
    ---------------------------------------
    def fib_recursion(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: 
        return F(n-1)+F(n-2)
    ---------------------------------------
    

def fib_generator(n):
    '''
    Generator version of fibonacci.
    '''

print(fib_loop(8))
print(fib_recursion(13))
print([i for i in fib_generator(14)])

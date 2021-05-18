def fib(n):

    if n <= 1:
      return n    
    else:
      return(fib(n-1) + fib(n-2))


def lucas(n):

    if n == 0:
      return 2

    elif n == 1:
      return 1
    
    elif n == 2:
      return 3
         
    else:
      return(lucas(n-1) + lucas(n-2))


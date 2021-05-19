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


def sum_series(x,y=0,z=1):

  if x == 0:
      return y
  if x == 1:
      return z 
  else:
    return(sum_series(x-1, y, z) + sum_series(x-2, y, z))
  


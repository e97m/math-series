
def calculate_fibonacci(n):
   if n <= 1:
       return n
   else:
       return(calculate_fibonacci(n-1) + calculate_fibonacci(n-2))


def fibonacci(n):
    series =[]
    if type(n) != int:
        return ("Please enter a positive integer")
    elif n <= 0:
        return ("Please enter a positive integer")
    else:
        for i in range(n):
            series.append(calculate_fibonacci(i))
        return (f'Fibonacci sequence upto the position {n} is: {series}')



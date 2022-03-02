
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




# def calculate_lucas(n):
#     if n == 1:
#         return 2
#     elif n == 2:
#         return 1
#     else:
#        return(calculate_lucas(n-1) + calculate_lucas(n-2))

# def lucas(n):
#     series =[]
#     if type(n) != int:
#         return ("Please enter a positive integer")
#     elif n <= 0:
#         return ("Please enter a positive integer")
#     else:
#         for i in range(n):
#             series.append(calculate_lucas(i))
#         return (f'Lucas sequence upto the position {n} is: {series}')


def lucas(n) :
    if type(n) != int:
        return ("Please enter a positive integer")
    elif n <= 0:
        return ("Please enter a positive integer")
    else:

        series = []
        a = 2
        b = 1
        
        if (n == 1) :
            series = [a]
            return (f'Lucas sequence upto the position {n} is: {series}')
        elif n == 2:
            series = [a, b]
            return (f'Lucas sequence upto the position {n} is: {series}')
        else:
            series.append(2)
            series.append(1)
            for i in range(2, n) :
                c = a + b
                a = b
                b = c
                series.append(b)
        return (f'Lucas sequence upto the position {n} is: {series}')


def calculate_fibonacci(n):
    '''
    Creat a fibonacci series
    input --> the currennt nth position (integer number)
    output --> the value of the nth potion in a fibonacci series
    '''
    if n <= 1:
       return n
    else:
       return(calculate_fibonacci(n-1) + calculate_fibonacci(n-2))


def fibonacci(n):
    '''
    Creat a fibonacci series to the nth position
    input --> the last nth position (integer number)
    output --> fibonacci series
    '''
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
#     if n <= 1:
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
    '''
    Creat a lucas series to the nth position
    input --> the last nth position (integer number)
    output --> lucas series
    '''
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


# def calculate_sum_series(n,a,b):
#     if n <= 1:
#         return a
#     elif n == 2:
#         return b
#     else:
#        return(calculate_sum_series(n-1) + calculate_sum_series(n-2))

# def sum_series(n):
#     series =[]
#     if type(n) != int:
#         return ("Please enter a positive integer")
#     elif n <= 0:
#         return ("Please enter a positive integer")
#     else:
#         for i in range(n):
#             series.append(calculate_sum_(i))
#         return (f'The sequence upto the position {n} is: {series}')


def sum_series(n, a=0, b=1):
    '''
    Creat a series starts with the value a and b, then to calculate the next value it summing the previous 2 values and keep doing this untill the nth position
    input --> the last nth position (int), the first value of series (int), the second value of series (int)
    output --> series
    '''
    if type(n) != int:
        return ("Please enter a positive integer")
    elif n <= 0:
        return ("Please enter a positive integer")
    else:
        series = []
        if (n == 1) :
            series = [a]
            return (f'The sequence upto the position {n} is: {series}')
        elif n == 2:
            series = [a, b]
            return (f'The sequence upto the position {n} is: {series}')
        else:
            series.append(a)
            series.append(b)
            for i in range(2, n) :
                c = a + b
                a = b
                b = c
                series.append(b)
        return (f'The sequence upto the position {n} is: {series}')


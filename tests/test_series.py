from math_series.series import fibonacci, lucas, sum_series

def test_fibonacci_0():
    actual = fibonacci(0)
    expected = 'Please enter a positive integer'
    assert(actual == expected)

def test_fibonacci_1():
    actual = fibonacci(1)
    expected = 'Fibonacci sequence upto the position 1 is: [0]'
    assert(actual == expected)

def test_fibonacci_2():
    actual = fibonacci(2)
    expected = 'Fibonacci sequence upto the position 2 is: [0, 1]'
    assert(actual == expected)

def test_fibonacci_3():
    actual = fibonacci(3)
    expected = 'Fibonacci sequence upto the position 3 is: [0, 1, 1]'
    assert(actual == expected)

def test_fibonacci_10():
    actual = fibonacci(10)
    expected = 'Fibonacci sequence upto the position 10 is: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]'
    assert(actual == expected)

def test_fibonacci_neg3():
    actual = fibonacci(-3)
    expected = 'Please enter a positive integer'
    assert(actual == expected)

def test_fibonacci_float():
    actual = fibonacci(3.3)
    expected = 'Please enter a positive integer'
    assert(actual == expected)

def test_fibonacci_a():
    actual = fibonacci('a')
    expected = 'Please enter a positive integer'
    assert(actual == expected)




def test_lucas_0():
    actual = lucas(0)
    expected = 'Please enter a positive integer'
    assert(actual == expected)

def test_lucas_1():
    actual = lucas(1)
    expected = 'Lucas sequence upto the position 1 is: [2]'
    assert(actual == expected)

def test_lucas_2():
    actual = lucas(2)
    expected = 'Lucas sequence upto the position 2 is: [2, 1]'
    assert(actual == expected)

def test_lucas_3():
    actual = lucas(3)
    expected = 'Lucas sequence upto the position 3 is: [2, 1, 3]'
    assert(actual == expected)

def test_lucas_10():
    actual = lucas(10)
    expected = 'Lucas sequence upto the position 10 is: [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]'
    assert(actual == expected)

def test_lucas_neg3():
    actual = lucas(-3)
    expected = 'Please enter a positive integer'
    assert(actual == expected)

def test_lucas_float():
    actual = lucas(3.3)
    expected = 'Please enter a positive integer'
    assert(actual == expected)

def test_lucas_a():
    actual = lucas('a')
    expected = 'Please enter a positive integer'
    assert(actual == expected)






def test_sum_series_0():
    actual = sum_series(0)
    expected = 'Please enter a positive integer'
    assert(actual == expected)

def test_sum_series_1():
    actual = sum_series(1)
    expected = 'The sequence upto the position 1 is: [0]'
    assert(actual == expected)

def test_sum_series_2():
    actual = sum_series(2)
    expected = 'The sequence upto the position 2 is: [0, 1]'
    assert(actual == expected)

def test_sum_series_3():
    actual = sum_series(3)
    expected = 'The sequence upto the position 3 is: [0, 1, 1]'
    assert(actual == expected)

def test_sum_series_10():
    actual = sum_series(10)
    expected = 'The sequence upto the position 10 is: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]'
    assert(actual == expected)

def test_sum_series_neg3():
    actual = sum_series(-3)
    expected = 'Please enter a positive integer'
    assert(actual == expected)

def test_sum_series_float():
    actual = sum_series(3.3)
    expected = 'Please enter a positive integer'
    assert(actual == expected)

def test_sum_series_a():
    actual = sum_series('a')
    expected = 'Please enter a positive integer'
    assert(actual == expected)

def test_sum_series_1_2_3():
    actual = sum_series(1, 2, 3)
    expected = 'The sequence upto the position 1 is: [2]'
    assert(actual == expected)

def test_sum_series_2_2_3():
    actual = sum_series(2, 2, 3)
    expected = 'The sequence upto the position 2 is: [2, 3]'
    assert(actual == expected)

def test_sum_series_3_2_3():
    actual = sum_series(3,2,3)
    expected = 'The sequence upto the position 3 is: [2, 3, 5]'
    assert(actual == expected)

def test_sum_series_6_2_3():
    actual = sum_series(6,2,3)
    expected = 'The sequence upto the position 6 is: [2, 3, 5, 8, 13, 21]'
    assert(actual == expected)

def test_sum_series_neg3_2_3():
    actual = sum_series(-3,2,3)
    expected = 'Please enter a positive integer'
    assert(actual == expected)

def test_sum_series_6_neg1_neeg2 ():
     actual = sum_series(6,-1,-2)
     expected = 'The sequence upto the position 6 is: [-1, -2, -3, -5, -8, -13]'
     assert(actual == expected)

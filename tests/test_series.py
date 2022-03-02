from math_series.series import fibonacci

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
from math_series.series import fib, lucas, sum_series


def test_fib1():
  actual = fib(0)
  expected = 0
  assert actual == expected

def test_fib2():
  actual = fib(2)
  expected = 1
  assert actual == expected

def test_fib3():
  actual = fib(4)
  expected = 3
  assert actual == expected

def test_lucas1():
  actual = lucas(0)
  expected = 2
  assert actual == expected

def test_lucas2():
  actual = lucas(1)
  expected = 1
  assert actual == expected

def test_lucas3():
  actual = lucas(4)
  expected = 7
  assert actual == expected

def test_lucas4():
  actual = lucas(3)
  expected = 4
  assert actual == expected

def test_sum():
  actual = sum_series(0)
  expected = 0
  assert actual == expected

def test_sum1():
  actual = sum_series(4)
  expected = 3
  assert actual == expected

def test_sum2():
  actual = sum_series(3, 2, 1)
  expected = 4
  assert actual == expected

def test_sum3():
  actual = sum_series(4, 2, 1)
  expected = 7
  assert actual == expected





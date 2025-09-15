"""
Problem #5 [Medium]

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair)
and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""
# We can implement car and cdr by passing appropriate functions to the pair function
# returned by cons. The car function will pass a function that returns the first element,
# while the cdr function will pass a function that returns the second element.
# Time complexity of O(1)
# Space complexity of O(1)
# where a and b are the elements of the pair.
from typing import Callable, Any


def car(pair: Callable[[Callable[[Any, Any], Any]], Any]) -> Any:
    return pair(lambda a, b: a)

def cdr(pair: Callable[[Callable[[Any, Any], Any]], Any]) -> Any:
    return pair(lambda a, b: b)

def cons(a: Any, b: Any) -> Callable[[Callable[[Any, Any], Any]], Any]:
    def pair(f: Callable[[Any, Any], Any]) -> Any:
        return f(a, b)
    return pair

# Tests:
def test_cons_car_cdr():
    pair = cons(3, 4)
    assert car(pair) == 3
    assert cdr(pair) == 4
    pair = cons('a', 'b')
    assert car(pair) == 'a'
    assert cdr(pair) == 'b'
    pair = cons(1.5, 2.5)
    assert car(pair) == 1.5
    assert cdr(pair) == 2.5

# Example usage:
if __name__ == "__main__":
    test_cons_car_cdr() # Run tests
    pair = cons(3, 4)
    print(car(pair)) # Output: 3
    print(cdr(pair)) # Output: 4


# Without using Callable
def car_no_callable(pair) -> Any:
    return pair(lambda a, b: a)

def cdr_no_callable(pair) -> Any:
    return pair(lambda a, b: b)

def cons_no_callable(a: Any, b: Any):
    def pair(f):
        return f(a, b)
    return pair

# Tests:
def test_cons_car_cdr_no_callable():
    pair = cons_no_callable(3, 4)
    assert car_no_callable(pair) == 3
    assert cdr_no_callable(pair) == 4
    pair = cons_no_callable('a', 'b')
    assert car_no_callable(pair) == 'a'
    assert cdr_no_callable(pair) == 'b'
    pair = cons_no_callable(1.5, 2.5)
    assert car_no_callable(pair) == 1.5
    assert cdr_no_callable(pair) == 2.5

# Example usage:
if __name__ == "__main__":
    test_cons_car_cdr_no_callable() # Run tests
    pair = cons_no_callable(3, 4)
    print(car_no_callable(pair)) # Output: 3
    print(cdr_no_callable(pair)) # Output: 4

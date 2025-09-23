"""
Problem #14 [Medium]

This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""
# We can estimate π using the Monte Carlo method by randomly generating points
# in a square that bounds a quarter circle and calculating the ratio of points
# that fall inside the quarter circle to the total number of points.
# The area of the quarter circle is (πr^2)/4 and the area of the square is r^2,
# so π can be estimated as 4 * (number of points inside the circle) / (total number of points).
# Time complexity of O(n)
# Space complexity of O(1)
# where n is the number of random points generated.
import random


def estimate_pi(num_samples: int) -> float:
    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_estimate = 4 * inside_circle / num_samples
    return round(pi_estimate, 3)

# Tests:
def test_estimate_pi():
    pi_value = estimate_pi(1000000)
    assert abs(pi_value - 3.141) < 0.01  # Allow a small margin of error
    pi_value = estimate_pi(10000)
    assert abs(pi_value - 3.141) < 0.1  # Allow a larger margin of error for fewer samples

# Example usage:
if __name__ == "__main__":
    test_estimate_pi() # Run tests
    print(estimate_pi(1000000))  # Output: Approximation of π to 3 decimal places

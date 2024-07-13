import numpy as np
import matplotlib.pyplot as plt

class Interval:

    def __init__(self, lb, ub=None):

        if ub is None:

            self.lb = self.ub = lb

        else:

            if lb > ub:

                raise ValueError("Left endpoint must not be greater than right.")

            self.lb = lb

            self.ub = ub



    def __str__(self):

        return f"[{self.lb}, {self.ub}]"



    def __repr__(self):

        return f"[{self.lb}, {self.ub}]"



    def __add__(self, other):

        if isinstance(other, Interval):

            return Interval(self.lb + other.lb, self.ub + other.ub)

        elif isinstance(other, (int, float)):

            return Interval(self.lb + other, self.ub + other)

        else:

            return NotImplemented



    def __radd__(self, other):

        return self.__add__(other)



    def __sub__(self, other):

        if isinstance(other, Interval):

            return Interval(self.lb - other.ub, self.ub - other.lb)

        elif isinstance(other, (int, float)):

            return Interval(self.lb - other, self.ub - other)

        else:

            return NotImplemented



    def __rsub__(self, other):

        if isinstance(other, (int, float)):

            return Interval(other - self.ub, other - self.lb)

        else:

            return NotImplemented



    def __mul__(self, other):

        if isinstance(other, Interval):

            results = [self.lb * other.lb, self.lb * other.ub, self.ub * other.lb, self.ub * other.ub]

            return Interval(min(results), max(results))

        elif isinstance(other, (int, float)):

            results = [self.lb * other, self.ub * other]

            return Interval(min(results), max(results))

        else:

            return NotImplemented



    def __rmul__(self, other):

        return self.__mul__(other)



    def __truediv__(self, other):

        if isinstance(other, Interval):

            if other.lb <= 0 <= other.ub:

                raise ZeroDivisionError("Division by an interval containing zero undefined.")

            if any(abs(bound) < 1e-297 for bound in [other.lb, other.ub]): # 1e-308
                raise OverflowError("Division results in an infinitely large interval.")
            
            results = [self.lb / other.lb, self.lb / other.ub, self.ub / other.lb, self.ub / other.ub]

            return Interval(min(results), max(results))

        elif isinstance(other, (int, float)):

            if other == 0:

                raise ZeroDivisionError("Division by zero is undefined.")

            if abs(other) < 1e-297:
                raise OverflowError("Division results in an infinitely large interval.")

            results = [self.lb / other, self.ub / other]

            return Interval(min(results), max(results))

        else:

            return NotImplemented



    def __rtruediv__(self, other):

        if isinstance(other, (int, float)):

            if self.lb <= 0 <= self.ub:

                raise ZeroDivisionError("Division by an interval containing zero is undefined.")

            if any(abs(bound) < 1e-297 for bound in [other.lb, other.ub]):
                raise OverflowError("Division results in an infinitely large interval.")

            results = [other / self.lb, other / self.ub]

            return Interval(min(results), max(results))

        else:

            return NotImplemented



    def __neg__(self):

        return Interval(-self.ub, -self.lb)



    def contains(self, value):

        return self.lb <= value <= self.ub

    def __pow__(self, exponent):
        if not isinstance(exponent, int):
            raise ValueError("Exponent must be an integer.")
    
        if exponent == 0:
            return Interval(1, 1)
    
        if exponent > 0:
            if exponent % 2 == 1:  # Odd exponent
                return Interval(self.lb ** exponent, self.ub ** exponent)
            else:  # Even exponent
                if self.lb >= 0:
                    return Interval(self.lb ** exponent, self.ub ** exponent)
                elif self.ub < 0:
                    return Interval(self.ub ** exponent, self.lb ** exponent)
                else:
                    return Interval(0, max(self.lb ** exponent, self.ub ** exponent))
    
        if exponent < 0:
            if self.lb <= 0 <= self.ub:
                raise ZeroDivisionError("Division by an interval containing zero is undefined.")
            results = [self.lb ** exponent, self.ub ** exponent]
            return Interval(min(results), max(results))



print("Task 3 test")

i = Interval (1,2)

print ( i ) # [1, 2]


print("\nTask 4 tests")

I1 = Interval(1, 4)  

I2 = Interval(-2, -1)  

print(I1)  # [1, 4]

print(I2)  # [-2, -1]

print(I1 + I2)  # [-1, 3]

print(I1 - I2)  # [2, 6]

print(I1 * I2)  # [-8, -1]

print(I1 / I2)  # [-4.0, -0.5]

print("\nTask 5 tests")
print(I1.contains(3))
print(I2.contains(-3))

print("\nTask 6 tests")
I1 = Interval(-1, 1) # contains 0
try:
    I1 = I2 / I1
except(ZeroDivisionError):
    print("Cant divide by an interval that contains 0")

try:
    I1 = I2 / 0
except(ZeroDivisionError):
    print("Cant divide interval by 0")

smallestPositiveNonZero = np.nextafter(0, 1)
numerator = Interval(1, 2)
denominator = Interval(smallestPositiveNonZero, 0.1)

try:
    result = numerator / denominator # Overflow
    print(result)
except(OverflowError):
    print("Resulting interval would be infinitely large")

try:
    result = numerator / smallestPositiveNonZero # Overflow
    print(result)
except(OverflowError):
    print("Resulting interval would be infinitely large")


print("\nTask 7 test")

j = Interval (1)

print ( j ) # [1, 1]


print("\nTask 8 tests")

I1 = Interval(2, 3)  

print(I1 + 1)  # [3, 4]

print(1 + I1)  # [3, 4]

print(1.0 + I1)  # [3.0, 4.0]

print(I1 + 1.0)  # [3.0, 4.0]

print(1 - I1)  # [-2, -1]

print(I1 - 1)  # [1, 2]

print(1.0 - I1)  # [-2.0, -1.0]

print(I1 - 1.0)  # [1.0, 2.0]

print(I1 * 1)  # [2, 3]

print(1 * I1)  # [2, 3]

print(1.0 * I1)  # [2.0, 3.0]

print(I1 * 1.0)  # [2.0, 3.0]

print(-Interval(4, 5))  # [-5, -4]

print("\nTask 9 tests")
x = Interval(-2, 2)
print(x ** 2)  # [0, 4]
print(x ** 3)  # [-8, 8]

# Task 10
xl = np.linspace(0., 1., 1000) # lower bound
xu = xl + 0.5 # upper bound
intervals = [Interval(xl[i], xu[i]) for i in range(len(xl))]

# Define the polynomial function p(I) = 3I^3 - 2I^2 - 5I - 1
def evaluate_polynomial(interval):
    return 3 * (interval ** 3) - 2 * (interval ** 2) - 5 * interval - 1

# Apply the function on al intervals
evaluated_intervals = [evaluate_polynomial(interval) for interval in intervals]

# Extract lower and upper bounds into yl & yu
yl = [interval.lb for interval in evaluated_intervals]
yu = [interval.ub for interval in evaluated_intervals]

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(xl, yl, color = "blue") # Lower boundaries
plt.plot(xl, yu, color = "green") # Upper boundaries
plt.xlabel('x')
plt.ylabel('p(I)')
plt.title(r'$p(I) = 3I^3 - 2I^2 - 5I - 1$, I = Interval(x, x+0.5)') # r (raw string) for LaTeX formatting
plt.ylim(-10, 4)
plt.xlim(0.0, 1.0)
plt.show()
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

            results = [self.lb / other.lb, self.lb / other.ub, self.ub / other.lb, self.ub / other.ub]

            return Interval(min(results), max(results))

        elif isinstance(other, (int, float)):

            if other == 0:

                raise ZeroDivisionError("Division by zero is undefined.")

            results = [self.lb / other, self.ub / other]

            return Interval(min(results), max(results))

        else:

            return NotImplemented



    def __rtruediv__(self, other):

        if isinstance(other, (int, float)):

            if self.lb <= 0 <= self.ub:

                raise ZeroDivisionError("Division by an interval containing zero is undefined.")

            results = [other / self.lb, other / self.ub]

            return Interval(min(results), max(results))

        else:

            return NotImplemented



    def __neg__(self):

        return Interval(-self.ub, -self.lb)



    def contains(self, value):

        return self.lb <= value <= self.ub



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


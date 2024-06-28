import math

def approx_ln(x, n):
    if x <= 0:
        raise ValueError("x must be greater than 0")
    if n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialization
    a = (1 + x) / 2
    g = math.sqrt(x)

    # Iteration
    for _ in range(n):
        a_next = (a + g) / 2 # a(i+1)
        g = math.sqrt(a_next * g) #g = g(i+1)
        a = a_next

    # Approximation
    ln_x_approx = (x - 1) / a
    
    return ln_x_approx

# Example usage
x = 4
n = 50
approx_ln_value = approx_ln(x, n)
print(f"The approximation of ln({x}) after {n} iterations is: {approx_ln_value}")


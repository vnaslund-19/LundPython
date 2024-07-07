import math
import numpy as np
import matplotlib.pyplot as plt

def approx_ln(x, n):
    # Initialization
    a = (1 + x) / 2
    g = math.sqrt(x)

    # Iteration
    for _ in range(n):
        a = (a + g) / 2 # a = a(i+1)
        g = math.sqrt(a * g) # g = g(i+1)

    # Approximation
    ln_x_approx = (x - 1) / a
    
    return ln_x_approx

def plot_ln_approximation_and_error(n):
    x_values = np.linspace(0.1, 1000, 10000) # creates 10000 evenly spaced values between 0.1 & 1000
    
    # Calculate the approximations and the differences
    approx_ln_values = np.array([approx_ln(x, n) for x in x_values])
    ln_values = np.log(x_values) # natural logarithm (base 10 would be np.log10())
    differences = ln_values - approx_ln_values

    # Create a figure with the two desired plots (1 row, 2 cols, 14x6 inches)
    figure, graphs = plt.subplots(1, 2, figsize=(14, 6))

    # Plot ln(x) and approx_ln(x) on the first subplot
    graphs[0].plot(x_values, ln_values, label='ln(x)', color='blue')
    graphs[0].plot(x_values, approx_ln_values, label=f'approx_ln(x, n={n})', color='red', linestyle='dashed')
    graphs[0].legend()
    graphs[0].set_title(f'Natural Logarithm vs Approximation (n={n})')
    graphs[0].set_xlabel('x')
    graphs[0].set_ylabel('Value')

    # Plot the difference on the second subplot
    graphs[1].plot(x_values, differences, label=f'Difference (n={n})', color='green')
    graphs[1].legend()
    graphs[1].set_title(f'Difference between ln(x) and approx_ln(x) (n={n})')
    graphs[1].set_xlabel('x')
    graphs[1].set_ylabel('Difference')

    figure.suptitle('Logarithm Approximation Analysis', fontsize=16)

    # Adjust layout
    plt.tight_layout()
    plt.show()

def get_user_input(prompt, value_type=float, condition=lambda x: True, error_message="Invalid input"):
    while True:
        try:
            value = value_type(input(prompt))
            if condition(value):
                return value
            else:
                print(error_message)
        except ValueError:
            print(error_message)

# TASK 1
print("TASK 1 (approx_ln)")
x = get_user_input("Enter the value of x (must be > 0): ", float, lambda v: v > 0, "x must be greater than 0.")
n_iterations = get_user_input("Enter the number of iterations n for approximation (must be a positive integer): ", int, lambda v: v > 0, "n must be a positive integer.")

approx_ln_value = approx_ln(x, n_iterations)
print(f"The approximation of ln({x}) after {n_iterations} iterations is: {approx_ln_value}")

# TASK 2
print("\nTASK 2 (plot approx & error)")
n_for_plot = get_user_input("Enter the number of iterations n for plotting (must be a positive integer): ", int, lambda v: v > 0, "n must be a positive integer.")
plot_ln_approximation_and_error(n_for_plot)

# TASK 3
x = 1.41
n_values = np.arange(1, 31)
approx_ln_values = np.array([approx_ln(x, n) for n in n_values])
abs_errors = np.abs(approx_ln_values - np.log(x))

plt.plot(n_values, abs_errors, label='error', color='red')
plt.legend()
plt.title('Absolute value of error versus n for x=1.41 (TASK 3)')
plt.xlabel('x')
plt.ylabel('Error')
plt.yscale('log')
plt.tight_layout()
plt.show()

# Task 4 
def fast_approx_ln(x, n):
    """

    """
    if x <= 0 or n < 1:
        raise ValueError("x must be larger than 0 and n must be larger or equal to 1")
    
    a = np.zeros(n + 1)
    d = np.zeros((n + 1, n + 1))
    
    a[0] = (x + 1) / 2
    g = np.sqrt(x)

    for i in range(n):
        a[i + 1] = (a[i] + g) / 2
        g = np.sqrt(a[i + 1] * g)

    d[0, :] = a

    for k in range(1, n + 1):
        for i in range(k, n + 1):
            d[k, i] = (d[k - 1, i] - 4**-k * d[k - 1, i - 1]) / (1 - 4**-k)
    
    return (x - 1) / d[n, n]

print("\nTASK 4 (fast_approx_ln)")
x = get_user_input("Enter the value of x (must be > 0): ", float, lambda v: v > 0, "x must be greater than 0.")
n_iterations = get_user_input("Enter the number of iterations n for approximation (must be a positive integer): ", int, lambda v: v > 0, "n must be a positive integer.")

fast_approx_ln_value = fast_approx_ln(x, n_iterations)
print(f"The approximation of ln({x}) after {n_iterations} iterations is: {fast_approx_ln_value}")

# Task 5
def plot_fast_ln(iterations_list, interval, num_points=1000):
    """

    """
    x = np.linspace(interval[0], interval[1], num_points)
    y = np.log(x)
    errs = [np.abs(y - [fast_approx_ln(_x, iterations) for _x in x]) for iterations in iterations_list]
            
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    for err, iterations in zip(errs, iterations_list):
        ax.plot(x, err, label=f'iteration {iterations}')
        
    ax.legend()
    ax.set_xscale('linear')
    ax.set_yscale('log')
    ax.set_xlabel('x')
    ax.set_ylabel('error')
    ax.set_title('Error behavior of the accelerated Carlsson method for the log (TASK 5)')
    ax.set_xlim(interval)
    ax.set_ylim([1e-17, 1e-2])
    ax.grid(True, which="both", ls="--")

    plt.show() 

plot_fast_ln([2, 3, 4, 5, 6], [0.01, 20], 1000)
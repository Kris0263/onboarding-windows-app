# test_calculations.py

def calculate_area_circle(radius):
    return 3.14 * radius * radius

def print_area_circle_1():
    area = 3.14 * 5 * 5
    print("Area 1:", area)

def print_area_circle_2():
    area = 3.14 * 7 * 7
    print("Area 2:", area)

### Refactored Code ###
# test_calculations.py

def calculate_area_circle(radius):
    return 3.14 * radius * radius

def print_area_circle(radius, label):
    area = calculate_area_circle(radius)
    print(f"{label}: {area}")

# Example usage:
print_area_circle(5, "Area 1")
print_area_circle(7, "Area 2")


def calculate_area_circle(radius):
    return 3.14 * radius * radius

def print_area_circle_1():
    area = 3.14 * 5 * 5
    print("Area 1:", area)

def print_area_circle_2():
    area = 3.14 * 7 * 7
    print("Area 2:", area)

### Poorly commneted code ###
# bad_comments.py

# function
def f(x):
    # calculate y
    y = x * 2 + 5
    # return
    return y

### good commented code ###

def calculate_final_score(x):
    """
    Calculates the final score based on input value x.
    Applies a multiplier of 2 and adds a fixed bonus of 5.
    """
    # Multiply input by 2 and add a fixed bonus
    final_score = x * 2 + 5
    return final_score

### bad error handling ###

def divide_by_two(x):
    return x / 2

### good error handling ###

def divide_by_two(x):
    """
    Safely divides a number by 2.
    Raises a ValueError if the input is not a number.
    """
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be a number.")
    
    return x / 2

def divide_by_two(x):
    try:
        return x / 2
    except TypeError:
        print("Error: Input must be a number.")
        return None

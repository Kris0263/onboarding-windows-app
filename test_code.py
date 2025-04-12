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

# test_calculations.py

def calculate_area_circle(radius):
    return 3.14 * radius * radius

def print_area_circle_1():
    area = 3.14 * 5 * 5
    print("Area 1:", area)

def print_area_circle_2():
    area = 3.14 * 7 * 7
    print("Area 2:", area)

### Simplicity  
Simplicity in coding means writing code that is easy to follow and free from unnecessary complexity. Avoiding redundant logic, minimizing dependencies, and using clear and concise constructs make code more approachable.  

### Readability  
Readable code is code that can be understood quickly by developers. Using meaningful variable and function names, proper indentation, and comments where necessary enhances readability. Code should be structured in a way that a developer unfamiliar with it can grasp its functionality with minimal effort.  

### Maintainability  
Maintainability ensures that code is easy to modify and extend over time. This involves writing modular and well-documented code, following best practices, and avoiding tightly coupled dependencies. The goal is to make future debugging and feature additions smooth and efficient.  

### Consistency  
Consistent code follows established coding conventions and style guides. Whether it’s naming conventions, indentation, or function structures, sticking to a uniform pattern makes collaboration easier and reduces confusion when working in teams.

### Efficiency  
Efficient code performs tasks optimally without unnecessary resource usage. Avoid premature optimizations but strive to write code that balances performance and maintainability. Proper data structures and algorithms should be used to ensure performance bottlenecks are minimized.  

MESSY CODE :  

def calc(x,y)
  if x > 10  
   if x > 5  
    return x * y  
   else:  
    return x + y  
   else:  
    return math.pow(x,y)  

CLEAN CODE :
def calculate_value(base: int, exponent: int) -> float
 """Performs different calculations based on input values."""
 if base > 10:
    return base * exponent if exponent < 5 else base + exponent
 return math.pow(base, exponent)

### Clean Code Reflections  
Consistent code formatting ensures that code is easier to read and maintain. It helps teams work together more efficiently, reduces misunderstandings, and minimizes the chance of bugs caused by inconsistent syntax. It also makes onboarding new developers smoother and speeds up code reviews.  

The linter detected several issues in my code, such as:  
- Unused variables  
- Missing `prop-types` in React components  
- Incorrect indentation  
- Use of `var` instead of `let` or `const`  
- Strings not using single quotes (per Airbnb rules)  

Yes, formatting the code with Prettier and fixing lint issues made it significantly easier to read. The consistent spacing, indentation, and quote usage helped improve clarity. It's also easier to spot logical errors when the code is neatly organized.  



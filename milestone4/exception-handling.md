### What are the best practices for exception handling in C#?
- Catch only the exceptions you can handle.
- Use specific exception types instead of general `Exception`.
- Avoid silent failures — log or inform the user.
- Use `finally` blocks for cleanup tasks.
- Do not use exceptions for flow control.
- Prefer defensive coding to prevent exceptions.

### How do try-catch-finally blocks work, and when should you use them?
- `try`: Encloses code that might throw an exception.
- `catch`: Handles the exception if one occurs.
- `finally`: Executes regardless of whether an exception occurred or not, often used for cleanup (e.g., closing files or database connections).

### What debugging tools in Visual Studio help diagnose runtime issues?   
- Breakpoints: Pause code execution at a specific line.   
- Step Into / Step Over: Walk through code line by line.  
- Watch & Locals Window: View and evaluate variables at runtime.  
- Call Stack: See the sequence of method calls.  
- Immediate Window: Execute code interactively while debugging.  

## Reflection

### Reflect on a time when proper exception handling prevented a major issue
During a file processing application, a user tried to upload a corrupted file. Because proper `try-catch` blocks were in place, the program caught the `IOException` and displayed a friendly error message. This prevented the application from crashing, maintained user trust, and avoided potential data loss.

###  What debugging techniques did you find most effective?
The most effective debugging techniques were:
- Setting **breakpoints** to pause execution and inspect values.
- Using **Step Over (F10)** to go through code without entering functions.
- Using the **Watch window** to monitor important variables.
- Observing the **Call Stack** to understand the sequence of method calls leading to an error.

These tools made it much easier to pinpoint exactly where and why errors occurred.

### How can you improve error logging and reporting in your code?
To improve error logging and reporting:
- Use structured logging frameworks like **Serilog** or **NLog**.
- Always log the full exception message, stack trace, and timestamp.
- Differentiate between user-facing messages and detailed internal logs.
- Set up alerts or monitoring systems for critical errors.
- Ensure that even unexpected exceptions are caught and logged in a safe way without exposing sensitive information.



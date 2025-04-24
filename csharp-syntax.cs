using System;

class Program
{
    static void Main()
    {
        // Integer type
        int intValue = 10;
        Console.WriteLine($"Integer Value: {intValue}");

        // Double type
        double doubleValue = 5.5;
        Console.WriteLine($"Double Value: {doubleValue}");

        // Boolean type
        bool boolValue = true;
        Console.WriteLine($"Boolean Value: {boolValue}");

        // Arithmetic operation
        double sum = intValue + doubleValue;
        Console.WriteLine($"Sum of {intValue} and {doubleValue} is {sum}");

        // Type conversion
        int explicitConversion = (int)doubleValue; // Explicit conversion
        Console.WriteLine($"Explicit Conversion of {doubleValue} to int: {explicitConversion}");

        double implicitConversion = intValue; // Implicit conversion
        Console.WriteLine($"Implicit Conversion of {intValue} to double: {implicitConversion}");

        // Potential pitfall: Overflow
        try
        {
            byte maxByte = 255;
            checked
            {
                maxByte += 1; // This will throw an OverflowException
            }
        }
        catch (OverflowException ex)
        {
            Console.WriteLine($"Overflow Exception: {ex.Message}");
        }
    }
}

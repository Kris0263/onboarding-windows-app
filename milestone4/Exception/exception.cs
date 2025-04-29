using System;
using System.IO;

class ExceptionDemo
{
    static void Main()
    {
        try
        {
            string content = File.ReadAllText("nonexistentfile.txt");
            Console.WriteLine(content);
        }
        catch (FileNotFoundException ex)
        {
            Console.WriteLine("Caught exception: " + ex.Message);
        }
        finally
        {
            Console.WriteLine("File operation attempted.");
        }
    }
}

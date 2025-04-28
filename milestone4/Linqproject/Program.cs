using System;
using System.Collections.Generic;
using System.Linq;

namespace CollectionsAndLinqDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // List of integers
            List<int> numbers = new List<int> { 5, 1, 8, 2, 9, 3 };

            // Dictionary mapping names to ages
            Dictionary<string, int> people = new Dictionary<string, int>()
            {
                {"Alice", 30},
                {"Bob", 25},
                {"Charlie", 35},
                {"David", 28}
            };

            // LINQ: Filter numbers greater than 4 and order them ascending
            var filteredNumbers = numbers.Where(n => n > 4).OrderBy(n => n);

            Console.WriteLine("Filtered and Sorted Numbers > 4:");
            foreach (var num in filteredNumbers)
            {
                Console.WriteLine(num);
            }

            Console.WriteLine("\nPeople aged over 28:");
            // LINQ: Find people older than 28
            var olderPeople = people.Where(p => p.Value > 28);

            foreach (var person in olderPeople)
            {
                Console.WriteLine($"{person.Key}: {person.Value} years old");
            }
        }
    }
}

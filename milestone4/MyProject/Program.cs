using System;

namespace MyProject
{
    // Base class
    public class Vehicle
    {
        public string Make { get; set; }
        public string Model { get; set; }

        public virtual void Drive()
        {
            Console.WriteLine("The vehicle is driving.");
        }
    }

    // Derived class 1
    public class Car : Vehicle
    {
        public override void Drive()
        {
            Console.WriteLine("The car is driving smoothly.");
        }
    }

    // Derived class 2
    public class Truck : Vehicle
    {
        public override void Drive()
        {
            Console.WriteLine("The truck is hauling heavy loads.");
        }
    }

    // Main program
    class Program
    {
        static void Main(string[] args)
        {
            Vehicle myVehicle = new Vehicle();
            myVehicle.Drive();

            Car myCar = new Car();
            myCar.Make = "Toyota";
            myCar.Model = "Camry";
            myCar.Drive();

            Truck myTruck = new Truck();
            myTruck.Make = "Ford";
            myTruck.Model = "F-150";
            myTruck.Drive();
        }
    }
}

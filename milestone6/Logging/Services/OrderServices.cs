using Serilog;
using System;

namespace MyApp.Services
{
    public class OrderService
    {
        public void ProcessOrder(int orderId)
        {
            try
            {
                Log.Information("Processing order {OrderId}", orderId);
                // Simulate error
                throw new InvalidOperationException("Database connection failed");
            }
            catch (InvalidOperationException ex)
            {
                Log.Error(ex, "Error occurred while processing order {OrderId}", orderId);
                throw;
            }
        }
    }
}

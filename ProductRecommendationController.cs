using System;
using System.Collections.Generic;

namespace ProductRecommendationApp
{
    public class ProductRecommendation
    {
        public string Category { get; set; }
        public string Product { get; set; }
        public decimal Price { get; set; }
        public string Description { get; set; }
        public bool IsAvailable { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            List<ProductRecommendation> productRecommendations = new List<ProductRecommendation>
            {
                new ProductRecommendation { Category = "Clothing", Product = "Shirt", Price = 29.99M, Description = "A cool shirt", IsAvailable = true },
                new ProductRecommendation { Category = "Shoes", Product = "Sneakers", Price = 79.99M, Description = "Comfortable sneakers", IsAvailable = true }
            };

            foreach (var product in productRecommendations)
            {
                Console.WriteLine($"{product.Category}: {product.Product} - {product.Price:C}");
            }
        }
    }
}

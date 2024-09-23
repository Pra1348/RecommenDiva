namespace RecommenDiva
{
    public class ProductRecommendation
    {
        public string Category { get; set; } // Category of the product
        public string Product { get; set; } // Name of the product
        public decimal Price { get; set; } // Price of the product
        public string? Description { get; set; } // Description of the product

        // Optional: Add additional properties relevant to the product
        public string? ImageUrl { get; set; } // URL for the product image
        public bool IsAvailable { get; set; } // Availability status
    }
}

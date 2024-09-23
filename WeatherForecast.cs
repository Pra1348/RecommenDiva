using System;
using System.ComponentModel.DataAnnotations;

namespace RecommenDiva
{
    public class WeatherForecast
    {
        [Key]
        public int Id { get; set; } // Unique identifier for the product

        [Required]
        [StringLength(100)]
        public string Category { get; set; } // Category of the product

        [Required]
        [StringLength(200)]
        public string Product { get; set; } // Name of the product

        [Range(0.01, double.MaxValue)]
        public decimal Price { get; set; } // Price of the product

        [StringLength(1000)]
        public string? Description { get; set; } // Description of the product

        [Url]
        public string? ImageUrl { get; set; } // URL for the product image

        public bool IsAvailable { get; set; } // Availability status

        public DateTime CreatedAt { get; set; } = DateTime.UtcNow; // Timestamp for when the product was created

        public DateTime? UpdatedAt { get; set; } // Timestamp for when the product was last updated
    }
}

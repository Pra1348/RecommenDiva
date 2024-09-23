using Microsoft.EntityFrameworkCore;
using RecommenDiva.Models;
using System.Collections.Generic;

namespace RecommenDiva.Data
{
    public class ApplicationDbContext : DbContext
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options) { }

        public DbSet<ProductRecommendation> ProductRecommendations { get; set; } // DbSet for ProductRecommendation
    }
}

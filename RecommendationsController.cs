using Microsoft.AspNetCore.Mvc;

namespace RecommenDiva.Controllers
{
    public class RecommendationsController : Controller
    {
        public IActionResult CollaborativeFiltering()
        {
            return View();
        }

        public IActionResult ContentBasedFiltering()
        {
            return View();
        }

        public IActionResult HybridFiltering()
        {
            return View();
        }

        public IActionResult BestSellingProducts()
        {
            return View();
        }

        public IActionResult CustomerDemographics()
        {
            return View();
        }

        public IActionResult DataCleaning()
        {
            return View();
        }

        public IActionResult EDA()
        {
            return View();
        }

        public IActionResult EvaluateModel()
        {
            return View();
        }

        public IActionResult Personalization()
        {
            return View();
        }

        public IActionResult RankBasedRecommendations()
        {
            return View();
        }

        public IActionResult UpsellingCrossSelling()
        {
            return View();
        }

        public IActionResult A_BTesting()
        {
            return View();
        }

        public IActionResult Conclusion()
        {
            return View();
        }
    }
}



using Microsoft.AspNetCore.Mvc;
using RecommenDiva.Services;

public class RecommendationController : Controller
{
    private readonly RecommendationService _recommendationService;

    public RecommendationController(RecommendationService recommendationService)
    {
        _recommendationService = recommendationService;
    }

    [HttpPost]
    public IActionResult GetRecommendations(string inputData)
    {
        var recommendations = _recommendationService.GetRecommendations(inputData);
        return Json(recommendations);
    }
}

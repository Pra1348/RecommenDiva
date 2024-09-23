using Microsoft.AspNetCore.Mvc;

namespace RecommenDiva.Controllers
{
    public class NewPageController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
    }
}

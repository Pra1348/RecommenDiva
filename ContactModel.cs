using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace RecommenDiva.Page
{
    public class ContactModel : PageModel
    {
        [BindProperty]
        public ContactForm Form { get; set; }

        public void OnGet()
        {
        }

        public IActionResult OnPost()
        {
            if (ModelState.IsValid)
            {
                // Process the form data here
                // For example, save it to the database or send an email

                return RedirectToPage("/Contact/Success"); // Redirect to a success page
            }

            return Page(); // If the form is not valid, redisplay the page with errors
        }
    }

    public class ContactForm
    {
        public string Name { get; set; }
        public string Phone { get; set; }
        public string Gender { get; set; }
        public string Email { get; set; }
        public DateTime Dob { get; set; }
        public bool Terms { get; set; }
        public string Address { get; set; }
        public string Categories { get; set; }
        public string Country { get; set; }
    }
}

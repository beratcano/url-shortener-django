import random
import string
from django.shortcuts import render, redirect
from .models import URL

def generate_short_code(length=7):
    """Generate a random alphanumeric string of a given length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_short_url(request):
    """
    Main view to display the form and handle the creation of a short URL.
    """
    if request.method == "POST":
        original_url = request.POST.get("original_url")
        if original_url:
            # Create a unique short code
            short_code = generate_short_code()
            while URL.objects.filter(short_code=short_code).exists():
                short_code = generate_short_code()
            
            # Create the URL object
            url = URL.objects.create(
                original_url=original_url,
                short_code=short_code
            )
            
            # We can pass the new URL to the template to show the user
            context = {
                "new_url": f"{request.scheme}://{request.get_host()}/{url.short_code}"
            }
            return render(request, "shortener/index.html", context)
            
    return render(request, "shortener/index.html")

def redirect_to_original(request, short_code):
    """
    Looks up the short code and redirects to the original URL.
    """
    try:
        url_object = URL.objects.get(short_code=short_code)
        return redirect(url_object.original_url)
    except URL.DoesNotExist:
        # For simplicity, we can render the main page with an error
        # In a real app, you might show a proper 404 page.
        context = {"error": "Short URL not found."}
        return render(request, "shortener/index.html", context, status=404)
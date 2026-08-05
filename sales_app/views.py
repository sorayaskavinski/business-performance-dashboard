from django.shortcuts import render


def home(request):
    """
    Display the application's home page.
    """

    return render(request, "home.html")
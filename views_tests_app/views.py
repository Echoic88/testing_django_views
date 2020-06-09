from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Display the main page
    """
    return render(request, "views_tests_app/index.html")
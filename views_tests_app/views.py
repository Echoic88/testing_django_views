from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import SuperHeroForm


# Create your views here.
def index(request):
    """
    Display the main page
    """
    if request.method == "POST":
        form = SuperHeroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Successful save")

        return redirect(reverse("views_tests_app:index"))

    else:
        form = SuperHeroForm()

    return render(request, "views_tests_app/index.html", {
        "form": form
    })

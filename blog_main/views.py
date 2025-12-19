from django.shortcuts import render


def home(request):
    # Logic for handling the home page request
    return render(request, "home.html")
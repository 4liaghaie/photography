from django.shortcuts import render
from .models import Landing
from .models import Fashion

def home(request):
    landings = Landing.objects.all()
    return render(request, "index.html", {"landings": landings})


def fashion(request):
    fashions = Fashion.objects.all()
    return render(request, "Fashion.html", {"fashions": fashions})

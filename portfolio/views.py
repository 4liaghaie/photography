from django.shortcuts import render
from .models import Landing, Landing1, Landing2
from .models import Fashion
from .models import Nature


def home(request):
    landings = Landing.objects.all()
    landings1 = Landing1.objects.all()
    landings2 = Landing2.objects.all()
    return render(request, "index.html", {"landings": landings, "landings2": landings2, "landings1": landings1})


def fashion(request):
    fashions = Fashion.objects.all()
    return render(request, "Fashion.html", {"fashions": fashions})


def nature(request):
    natures = Nature.objects.all()
    return render(request, "nature.html", {"natures": natures})


def about(request):
    return render(request, "about.html")



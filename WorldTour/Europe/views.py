from django.shortcuts import render
from django.http import HttpResponse
from .models import Trip
import arxiv


# Create your views here.
def index(request):
    context = {"trips": Trip.objects.all()}
    return render(request, "trips/index.html", context)

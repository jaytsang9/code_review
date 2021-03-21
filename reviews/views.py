from django.shortcuts import render
from django.http import HttpResponse
from .models import Review

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {'reviews': reviews}
    return render(request, 'reviews/reviews.html', context)
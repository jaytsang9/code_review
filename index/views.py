from django.shortcuts import render
from django.http import request, HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from reviews.models import Review, ReviewForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    reviews = Review.objects.all()
    context = {'reviews': reviews}
    return render(request, 'index/home.html', context)

def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = ReviewForm()
    return render(request, 'index/create.html', {'form':form})

def py_reviews(request):
    reviews = Review.objects.filter(language='Python')[0]
    data = {
        "title": reviews.title,
        "user": reviews.user,
        "language": reviews.language,
    }

    return JsonResponse(data)

def show_review(request, num):
    review = Review.objects.filter(id=num)
    context = {'review': review}
    return render(request, "index/review.html", context)

def login(request):

    return render(request, "index/login.html")

def register(request):
    return render(request, "index/register.html")


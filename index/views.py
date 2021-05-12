from django.shortcuts import render
from django.http import request, HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from reviews.models import Review, ReviewForm 
from django.contrib.auth.decorators import login_required

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
        "user": reviews.author,
        "language": reviews.language,
    }

    return JsonResponse(data)

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "index/register.html")

def login(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "index/login.html")
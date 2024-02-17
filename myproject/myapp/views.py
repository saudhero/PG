from django.shortcuts import render, redirect
from .models import User



def registration(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        phone_number = request.POST['phone_number']
        username = request.POST['username']

        # Check if a user with the same email already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'myapp/registration.html', {'error': 'الايميل موجود'})

        # Check if a user with the same phone number already exists
        if User.objects.filter(phone_number=phone_number).exists():
            return render(request, 'myapp/registration.html', {'error': 'User with the same phone number already exists.'})

        # Check if a user with the same username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'myapp/registration.html', {'error': 'User with the same username already exists.'})

        user = User(email=email, password=password, phone_number=phone_number, username=username)
        user.save()

        return redirect('myapp:login')

    return render(request, 'myapp/registration.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email, password=password)
            return redirect('myapp:home')
        except User.DoesNotExist:
            return render(request, 'myapp/login.html', {'error': 'غلط ياحمار.'})

    return render(request, 'myapp/login.html')

def home(request):
    return render(request, 'myapp/home.html')

def phishing_detection(request):
    # Logic to fetch and process data for phishing detection
    return render(request, 'services/phishing_detection.html')

def articles(request):
    # Logic to fetch and process data for articles
    return render(request, 'services/articles.html')

def video(request):
    # Logic to fetch and process data for video
    return render(request, 'services/video.html')
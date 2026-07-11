from django.shortcuts import render, redirect
from .models import Donor


def home(request):
    return render(request, 'home.html')

def register(request):

    if request.method == "POST":

        name = request.POST.get('name')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        blood = request.POST.get('blood')
        state = request.POST.get('state')
        city = request.POST.get('city')
        password = request.POST.get('password')

        Donor.objects.create(
            name=name,
            gender=gender,
            email=email,
            phone=phone,
            blood=blood,
            state=state,
            city=city,
            password=password
        )

        return render(request, 'register.html', {'success': True})

    return render(request, 'register.html')

def login_view(request):

    if request.method == "POST":

        phone = request.POST.get('phone').strip()
        password = request.POST.get('password').strip()

        print(phone)
        print(password)

        user = Donor.objects.filter(
            phone=phone,
            password=password
        ).first()

        print(user)

        if user:

            return render(request, 'login.html', {
                'success': True
            })

        else:

            return render(request, 'login.html', {
                'error': 'Invalid Phone or Password'
            })

    return render(request, 'login.html')
def search(request):

    donors = []

    if request.method == "POST":

        blood = request.POST.get('blood')

        donors = Donor.objects.filter(blood=blood)

    return render(request, 'search.html', {'donors': donors})

def about(request):
    return render(request, 'aboutus.html')

def contact(request):
    return render(request, 'contactus.html')

def logout(request):

    return render(request, 'logout.html')
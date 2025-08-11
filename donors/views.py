from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, DonorForm, BloodRequestForm
from django.contrib.auth import authenticate, login, logout
from .models import Donor, BloodRequest

def register_donor(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        donor_form = DonorForm(request.POST)
        if user_form.is_valid() and donor_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            donor = donor_form.save(commit=False)
            donor.user = user
            donor.save()
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
        donor_form = DonorForm()
    return render(request, 'register.html', {'user_form': user_form, 'donor_form': donor_form})

def donor_login(request):
    if request.method == "POST":
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(request, username=uname, password=pwd)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def request_blood(request):
    if request.method == "POST":
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BloodRequestForm()
    return render(request, 'request_blood.html', {'form': form})

def donor_list(request):
    donors = Donor.objects.all()
    blood_group = request.GET.get('blood_group')
    city = request.GET.get('city')
    if blood_group:
        donors = donors.filter(blood_group=blood_group)
    if city:
        donors = donors.filter(city__icontains=city)
    return render(request, 'donor_list.html', {'donors': donors})

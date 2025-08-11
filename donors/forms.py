from django import forms
from django.contrib.auth.models import User
from .models import Donor, BloodRequest

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['blood_group', 'contact', 'city', 'last_donated']

class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = '__all__'

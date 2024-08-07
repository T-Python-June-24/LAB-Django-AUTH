from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'input input-bordered w-full'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input input-bordered w-full'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input input-bordered w-full'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input input-bordered w-full'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            if self.fields[fieldname].label:
                self.fields[fieldname].label = self.fields[fieldname].label.capitalize()

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    email = forms.EmailField()
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = Profile
        fields = ['phone_number', 'address', 'date_of_birth', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        profile = super(UserProfileForm, self).save(commit=False)
        profile.user.email = self.cleaned_data['email']
        if commit:
            profile.user.save()
            profile.save()
        return profile

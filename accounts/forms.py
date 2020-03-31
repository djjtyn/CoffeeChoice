from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

"""Form to be used for logging users in"""
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
"""Form used to register a new user"""
class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput)

    """Form has email, username, password and password confirmation areas to be filled by user"""  
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
    
    """email and username values taken from form user fills out and assigned to corresponding variables""" 
    """If email already in use, user gets an error"""
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError('Email address must be unique')
        return email

    """Password sections values taken from form user fills out and assigned to corresponding variables"""
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        """If one of the password fields is empty the user receives an error"""
        if not password1 or not password2:
            raise ValidationError("Please confirm your password")
        
        """If passwords differ from each other the user receives an error"""
        if password1 != password2:
            raise ValidationError("Passwords must match")
        return password2
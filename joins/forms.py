from django import forms
from django.core.files.images import get_image_dimensions
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from joins.models import UserProfile
from django import *
from django.contrib.auth import authenticate, get_user_model, login, logout

from .models import *
User = get_user_model()

class CompanyForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = [
            'rootid',
            'name',
            'phone',
            'email',
            'address',
            'city',
            'logo',
            'user'
            ]

class AvatarForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'tracker',
            'rootid',
            'gender',
            'phone',
            ]

class AcctForm(forms.ModelForm):
    class Meta:
        model = t_accts
        fields = [
            'fname',
            'lname',
            'gender',
            'account_type',
            'acct_company',
            'user',
            ]

class EditAcctForm(forms.ModelForm):
    class Meta:
        model = t_accts
        fields = [
            'fname',
            'middle_name',
            'lname',
            'gender',
            'phone',
            'dob',
            'address',
            'emergency_contact',
            'email',
            ]

class EditClientAttributeForm(forms.ModelForm):
    class Meta:
        model = t_client_attribute
        fields = [
            'client_number',
            'company',
            'soc',
            ]




class UserForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = [
            'rootid',
            'gender',
            'avatar',
            ]
   


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]


    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")

        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return email



class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False, widget = forms.TextInput(attrs={'class' : 'form-control form-control-sm','placeholder':'Username'}), label='')
    
    first_name = forms.CharField(max_length=30, required=False, widget = forms.TextInput(attrs={'class' : 'form-control form-control-sm','placeholder':'First Name'}), label='')
    last_name = forms.CharField(max_length=30, required=False, widget = forms.TextInput(attrs={'class' : 'form-control form-control-sm','placeholder':'Last Name'}), label='')
    email = forms.EmailField(max_length=254, required=False,  widget = forms.TextInput(attrs={'class' : 'form-control form-control-sm','placeholder':'Email'}), label='')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control form-control-sm','placeholder':'Password'}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control form-control-sm','placeholder':'Repeat Password'}), label='')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )



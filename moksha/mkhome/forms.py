from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Account,UserProfile




class RegistrationForm(forms.ModelForm): 
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'enter password','class':'form-control'
        }))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'confirm password','class':'form-control'
        }))
 
    class Meta:
        model = Account
        fields=['first_name','last_name','phone_number','email','password']

    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        # self.fields['first_name'].widget.attrs['placeholder'] = 'first_name'
        # self.fields['last_name'].widget.attrs['placeholder'] = 'last_name'
        # self.fields['phone_number'].widget.attrs['placeholder'] = 'phone_number'
        # self.fields['email'].widget.attrs['placeholder'] = 'email'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'forms-control'


    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password=cleaned_data.get('password')
        confirm_password =cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                'password does not match!'
            )

class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name','last_name','phone_number')


    def __init__(self,*args,**kwrgs):
        super(UserForm,self).__init__(*args,**kwrgs)
        for field in self.fields:
            self.fields[field].widget.attrs['clear'] ='form-control'

class UserProfileForm(forms.ModelForm):
    class Meta: 
        model = UserProfile
        fields = ('address_line_1','address_line_2','city','state','country','profile_picture')

    def __init__(self,*args,**kwrgs):
        super(UserProfileForm,self).__init__(*args,**kwrgs)
        for field in self.fields:
            self.fields[field].widget.attrs['clear'] ='form-control'



        
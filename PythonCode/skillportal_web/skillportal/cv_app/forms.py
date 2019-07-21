from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phone_field import PhoneField
from .models import Candidate


class UserLoginForm(forms.Form):
    user =forms.CharField(label= 'user',max_length = 100)
    email = forms.EmailField(label='email',required=True,)
    password = forms.CharField(label='password',required=True, max_length=32, widget=forms.PasswordInput())

class UserSignup(forms.ModelForm):
    # name = forms.CharField(label ='name',max_length=30,required=True,)
    # fname = forms.CharField(label='fname',max_length=30)
    # lname = forms.CharField(label='lname',max_length=30)
    # email = forms.EmailField(label='email',max_length=254,help_text='Enter a valid email address.')
    # phone = PhoneField(help_text='Required!! Contact Number')
    # password1 = forms.CharField(label='password1',required=True, max_length=32, widget=forms.PasswordInput())
    # password2 = forms.CharField(label='password2',required=True,max_length=32, widget=forms.PasswordInput())

    class Meta:
        model = Candidate
        fields = '__all__'
        # fields = ('username', 'first_name','last_name','email','password1','password2',)

    # def save(self, commit=True):
    #     user = User.objects.create_user(
    #         self.cleaned_data['username'],
    #         self.cleaned_data['email'],
    #         self.cleaned_data['password']
    #     )
    #     return user
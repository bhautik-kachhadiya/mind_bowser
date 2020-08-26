from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from manager_app import models
from django.forms.widgets import DateInput,EmailInput
from django.contrib.auth.forms import AuthenticationForm,UsernameField


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Email',
        widget=forms.EmailInput(attrs={'type': 'email'})
    )

class ManagerCreateForm(UserCreationForm):
    class Meta():
        fields = ('first_name', 'last_name', 'username',
                  'dob', 'company', 'address', 'password1', 'password2',)
        model = models.Manager
        labels = {
            'dob': ('D.O.B'),
            'username' : ('Email')
        }
        widgets = {
            'dob': DateInput(attrs={'type': 'date'}),
            'username': EmailInput(attrs={'type': 'email'})
        }

class EmployeeForm(forms.ModelForm):
    class Meta():
        fields = ('first_name', 'last_name', 'email',
                  'mobile', 'dob', 'address','city')
        model = models.Employee
        labels = {
            'dob' : ('D.O.B')
        }
        widgets = {
            'dob': DateInput(attrs={'type' : 'date'})
        }


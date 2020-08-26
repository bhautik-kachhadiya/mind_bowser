from django.shortcuts import render
from django.http import HttpResponse 
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from assignment_1 import settings

from django.views.generic import (
    CreateView, ListView, UpdateView, DeleteView, TemplateView)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from manager_app import models
from manager_app import forms
from django.forms.widgets import DateInput,EmailInput

# method for send the email
from django.core.mail import send_mail

# Create your views here.


class CustomAuthViews(LoginView):
    """
    Extended the functionality of Inbuilt
    Authentication Login Views
    """
    login_url = 'manager_app:login'
    authentication_form = forms.CustomAuthenticationForm
    template_name = 'login.html'


class Index(TemplateView):
    """
    class will invoke when
    user start the project
    """
    template_name = 'index.html'

class SignUp(CreateView):
    """
    using this class manager can signUp
    """
    try:
        template_name = 'signup.html'
        form_class = forms.ManagerCreateForm
        success_url = reverse_lazy('manager_app:login')
    except Exception:
        print('Exception Occurs in Signup')


class Welcome(TemplateView):
    """
    after Login this class will invoke
    and welcomepage will display
    """
    template_name = 'welcome.html'

class Thanks(TemplateView):
    """
    When user logout 
    Thanks Page will Display
    """
    template_name = 'thanks.html'


class EmployeeEntry(CreateView,LoginRequiredMixin):
    """
    this class Manager can enter new Employee 
    """
    try:
        login_url = 'manager_app:login'
        template_name = 'employee_form.html'
        form_class = forms.EmployeeForm
        success_url = reverse_lazy('manager_app:employee_success')
    except Exception:
        print('exception Occurs in Employee Entry')

class EmployeeList(ListView,LoginRequiredMixin):
    """
    This class is responsible for Displaying 
    Employee List
    """
    try:
        login_url = 'manager_app:login'
        model = models.Employee
        template_name = 'employee_list.html'
        context_object_name = 'employees'
    except Exception:
        print('Exception Occurs in Employee List')


class EmployeeUpdate(UpdateView,LoginRequiredMixin):
    """
    this class is responsible for
    Update the Employees
    """
    try:
        login_url = 'manager_app:login'
        model = models.Employee
        template_name = 'update_employee.html'
        fields = ('first_name', 'last_name', 'email',
                'mobile', 'dob', 'address', 'city')

        def get_form(self, form_class=forms.EmployeeForm):

            form = super(EmployeeUpdate,self).get_form(forms.EmployeeForm)
            form.fields['dob'].widget.attrs.update({'class' : 'datepicker'})
            return form
    except Exception:
        print('Exception Occurs in Employee Update Feature')

    
class EmployeeDelete(DeleteView,LoginRequiredMixin):
    """
    this class is invoke when manager wants to Delete the employee
    """
    try:
        login_url = 'manager_app:login'
        model = models.Employee
        template_name = 'delete_confirm.html'
        success_url = reverse_lazy('manager_app:employee_list')
    except Exception:
        print('Exception Occurs in Employ Delete Feature')
    


@login_required
def employeeSuccess(request):
    """
    when manager add new Employee
    The success Page will display and
    the new Employee Will get email
    """    
    user_mail = models.Employee.objects.latest('pk')
    try:
        """
        the new Employee Will get email
        """
        send_mail('Welcome To The Company',
            'hey,\nWelcome To The Company \n Your data is successfully Enterd in Employee Table by Manager.\n Your skills and telents will be agreate addition to our company.',
            settings.EMAIL_HOST_USER, [user_mail, ], fail_silently=False)
        
    except Exception:
        print('Error Occurs in sending mail.\n Please check Internet Connection or,\n Enter email and password in Settings.pyfile')
    
    return render(request,'employee_success.html')


@login_required
def search(request):
    """
    this function will return all results of related search
    """
    try:
        qur = request.GET.get('search').lower()
        result = [item for item in models.Employee.objects.all() if qur in item.first_name.lower() or qur in item.last_name.lower()]
        return render(request,'search.html',{'employees':result})
        
    except Exception:
        print('Exception Occurs in Search...')

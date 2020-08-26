from django.conf.urls import url
from django.urls import path
from manager_app import views
from django.contrib.auth import views as auth_views

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


app_name = 'manager_app'

urlpatterns = [
    url(r'^$',views.Index.as_view(),name = 'index'),
    
    # URLS for Authentication
    url(r'^signup/$',views.SignUp.as_view(),name = 'signup'),
    url(r'^login/$', views.CustomAuthViews.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    
    # URLS for CREATE,READ,UPDATE and DELETE (CRUD)
    url(r'^insert_employee/$',views.EmployeeEntry.as_view(),name = 'new_employee'),
    url(r'^employee_list/$',views.EmployeeList.as_view(),name = 'employee_list'),
    url(r'^update_employee/(?P<pk>\d+)/$',views.EmployeeUpdate.as_view(),name= 'update_employee'),
    url(r'^delete_employee/(?P<pk>\d+)/$',views.EmployeeDelete.as_view(),name= 'delete_employee'),
    
    # URLS For Searching and Send mail/Success Page.
    url(r'^search/$',views.search,name = 'search'),
    url(r'^employee_success/$', views.employeeSuccess, name='employee_success'),


    #JWT Token
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/token/refresh/',TokenRefreshView.as_view())
]

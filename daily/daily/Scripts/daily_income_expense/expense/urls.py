"""
URL configuration for daily_income_expense project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('expense',v.add_expense,name='add1'),
    path('exp_list',v.expense_list,name='elist'),
    path('expense_search',v.exp_search,name='expense_search'),
    path('ext/<str:ext2>',v.sort_by_type,name='ext1')
]   

"""
URL configuration for crud_project project.

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
    path('',v.home),
    path('emp_details',v.emp_details),
    path('emp_account',v.emp_account),
    path('emp_list',v.emp_list),
    path('delete1',v.delete_1),
    path('delete2/<int:eid>',v.delete_2),
    path('edit/<int:eid>',v.edit),
    path('act_list',v.act_list),
    path('delete/<int:eid>',v.delete),
    path('edit1/<int:eid>',v.edit_1),
]

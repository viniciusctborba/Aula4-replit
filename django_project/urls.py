"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from appdovinicius import views
from django.urls import path

urlpatterns = [
  path('', views.home, name="home"),
  path('admin/', admin.site.urls),
  path('livros', views.create_livro),
  path('livros/update/<id>', views.update_livro),
  path('livros/delete/<id>', views.delete_livro),
  path('hobby', views.create_hobby),
  path('hobby/update/<id>', views.update_hobby),
  path('hobby/delete/<id>', views.delete_hobby),
]




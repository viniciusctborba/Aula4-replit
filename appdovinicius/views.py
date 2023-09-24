from django.shortcuts import render, redirect
from .models import Livros, Hobby, Pais
from .forms import DistrosForm

def home(request):
  livros = Livros.objects.all()
  hobby = Hobby.objects.all()
  pais = Pais.objects.all()
  return render(request, "home.html", context={
    "livros": livros,
    "hobby": hobby,
    "pais": pais
  })
  # views.py


def create_livro(request):
  if request.method == "POST":
    Livros.objects.create(
    title = request.POST["title"],
    escritor = request.POST["writer"],
    genre = request.POST["genre"],
    release_date = request.POST["release_date"]
  )
    return redirect("home")
  return render(request, "forms.html", context={"action":"adicionar"})

def update_livro(request, id):
  livro = Livros.objects.get(id = id)
  
  if request.method == "POST":
    livro.title = request.POST["title"]
    livro.escritor = request.POST["writer"]
    livro.genre = request.POST["genre"]
    livro.release_date = request.POST["release_date"]
    livro.save()
    return redirect("home")
  return render(request, "forms.html", context={"action":"atualizar", "livro": livro })


def delete_livro(request, id):
  livro = Livros.objects.get(id = id)  
  if request.method == "POST":
    if "confirm" in request.POST:
      livro.delete()
     
  return redirect("home")
  return render(request, "are_you_sure.html", context={"livro": livro })



def create_hobby(request):
  if request.method == "POST":
    Hobby.objects.create(
    title = request.POST["title"],
    priority = request.POST["priority"],
    how_often = request.POST["how_often"],
    category = request.POST["category"]
  )
    return redirect("home")
  return render(request, "forms2.html", context={"action":"adicionar"})


def update_hobby(request, id):
  hobby = Hobby.objects.get(id = id)
  
  if request.method == "POST":
    hobby.title = request.POST["title"]
    hobby.priority = request.POST["priority"]
    hobby.how_often = request.POST["how_often"]
    hobby.category = request.POST["category"]
    hobby.save()
    return redirect("home")
  return render(request, "forms2.html", context={"action":"atualizar", "hobby": hobby })


def delete_hobby(request, id):
  hobby = Hobby.objects.get(id = id)  
  if request.method == "POST":
    if "confirm" in request.POST:
      hobby.delete()
     
  return redirect("home")
  return render(request, "are_you_sure.html", context={"hobby": hobby })


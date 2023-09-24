from django.db import models


# models.py


class Distros(models.Model):
    name = models.CharField(max_length=100)
    available = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Livros(models.Model):
  title = models.CharField(max_length=50)
  escritor = models.CharField(max_length=70)
  genre = models.CharField(max_length=20)
  release_date = models.DateField()

class Hobby(models.Model):
  OPTIONS = [
    ("N", "Never"),
    ("S", "Sometimes"),
    ("A", "Always"),
  ]
  CATEGORY = [
    ("F", "Fun"),
    ("H", "Health"),
  ]
  title = models.CharField(max_length=50)
  how_often = models.CharField(max_length=1, choices=OPTIONS)
  priority = models.IntegerField()
  category = models.CharField(max_length=1, choices=CATEGORY)

class Pais(models.Model):
  cidade = models.CharField(max_length=50)
  pais = models.CharField(max_length=70)
  continente = models.CharField(max_length=50)



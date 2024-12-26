from django.db import models
from django.contrib.auth.models import User

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    categoria = models.CharField(max_length=50)
    descripcion = models.TextField(null=True) 
    
    def __str__(self):
        return self.nombre 
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} - {self.telefono} - {self.email}"
    
class Mascota(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    especie = models.CharField(max_length=50, choices=[
        ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('pez', 'Pez'),
        ('ave', 'Ave'),
        ('reptil', 'Reptil'),
    ])
    raza = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    historial = models.TextField(null=True) 

    def __str__(self):
        return f"{self.especie} - {self.nombre} - {self.edad}"
    
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="profile_picture/", null=True, blank=True)





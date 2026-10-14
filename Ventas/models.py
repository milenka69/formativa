from django.db import models

class Cliente (models.Model):
    rut = models.CharField(max_length=12, primary_key=True, unique=True)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    numero_telefono =models.CharField()

    def __str__(self):
        return self.nombre

class Pedido (models.Model):
    ID =  models.AutoField(primary_key=True)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
    )
    fecha = models.DateField()
    total = models.PositiveIntegerField()

    def __str__(self):
        return f"Pedido {self.ID} - Cliente: {self.cliente.nombre}"

    
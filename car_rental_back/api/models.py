from django.db import models

class CarCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    price_per_day = models.FloatField()
    available_units = models.IntegerField()
    is_available = models.BooleanField(default = True)
    category = models.ForeignKey(CarCategory, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return f"{self.brand} {self.model}"
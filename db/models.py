from django.db import models


class Car(models.Model):
    ENGINE_TYPE = (
        ("ICE", "internal combustion engine"),
        ("HYBRID", "hybrid engine"),
        ("ELECTRICAL", "electric engine"),
    )

    brand = models.CharField(max_length=255, unique=True)
    horse_power = models.IntegerField()
    creation_date = models.DateField(null=True)
    description = models.TextField(default="Bla bla bla")
    engine_type = models.CharField(max_length=10, choices=ENGINE_TYPE, null=True)
    created_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f"{self.id} {self.brand} (power: {self.horse_power})"

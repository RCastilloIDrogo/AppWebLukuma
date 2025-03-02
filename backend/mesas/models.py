from django.db import models

class Mesa(models.Model):
    numero = models.IntegerField(unique=True)
    qr_code = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"Mesa {self.numero}"

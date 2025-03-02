from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = [
        ('admin', 'Administrador'),
        ('mesero', 'Mesero'),
        ('cocinero', 'Cocinero'),
    ]
    rol = models.CharField(max_length=20, choices=ROLES, default='mesero')

    # Solución al error de reverse accessor conflicts
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="usuarios_groups",  # Cambia el nombre del reverse accessor
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="usuarios_permissions",  # Cambia el nombre del reverse accessor
        blank=True
    )

    def __str__(self):
        return f"{self.username} - {self.rol}"

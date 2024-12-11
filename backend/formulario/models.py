import datetime
from typing import Optional
from django.db import models
from .constantes import GRAUS_ENSINO, USER_CATEGORIES


class UserCategory(models.Model):
    user_data_category: models.CharField = models.CharField(
        max_length=100, choices=[(cat, cat) for cat in USER_CATEGORIES]
    )

    def __str__(self):
        return f"{self.user_data_category}"


class UserData(models.Model):

    nome: models.CharField = models.CharField(max_length=100)
    email: models.CharField = models.EmailField(
        max_length=100, unique=True, default="user@example.com"
    )
    numero: models.CharField = models.CharField(max_length=100)
    idade: models.IntegerField = models.IntegerField()
    grau_ensino: models.CharField = models.CharField(
        max_length=100,
        choices=[(grau, grau) for grau in GRAUS_ENSINO],
        default="Não informado",
    )
    mensagem: models.CharField = models.CharField(max_length=256)
    user_category_id: models.ForeignKey = models.ForeignKey(
        UserCategory, on_delete=models.PROTECT, default=None, related_name="category"
    )
    data_registro: models.DateTimeField = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User: {self.nome} [{self.user_category_id}] email: {self.email} "

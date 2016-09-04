from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Bicicleta(models.Model):
    COM_MARCHA = 'Com Marcha'
    SEM_MARCHA = 'Sem Marcha'
    MARCHA_CHOICES = (
        (COM_MARCHA, 'Com Marcha'),
        (SEM_MARCHA, 'Sem Marcha'),
    )

    fabricante = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    marcha = models.CharField(max_length=10,
                              choices=MARCHA_CHOICES,
                              default=SEM_MARCHA,
                              )
    marcaDoCambio = models.CharField(max_length=100)
    dono = models.CharField(max_length=100)

    # celular = models.RegexField(regex=r'^\+?1?\d{9,15}$', error_message=("Digite um número de celular válido"))
    celular = PhoneNumberField()
    email = models.EmailField(max_length=100)

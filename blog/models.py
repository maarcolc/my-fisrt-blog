from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Post(models.Model): #Define el modelo de datos
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #Relacion con otro modelo
    title = models.CharField(max_length=200) #Define un texto con un numero limitado de caracteres
    text = models.TextField() #Define un texto largo sin limite
    created_date = models.DateTimeField( #Define una fecha y hora
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UsuarioManager

class Usuario(AbstractUser):
    address = models.CharField(max_length=200, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, blank=False, null=False)
    
    USERNAME_FIELD = 'email'
    
    

    REQUIRED_FIELDS = [] #vai precisar somente do email para criar superuser

    objects = UsuarioManager()

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.username

#TODO: consertar upload_to

class Servico(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=100, blank=False, null=False)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to=f"servicesImages/", blank=True, null=True)


    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    def __str__(self):
        return f'{self.titulo} - {self.usuario.username}'
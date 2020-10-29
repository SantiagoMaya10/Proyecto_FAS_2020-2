from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    class Sexo(models.TextChoices):
        FEMENINO = 'F', _('Femenino')
        MASCULINO = 'M', _('Masculino')
        NOBINARIO = 'X', _('No binario')

    class Tipo(models.TextChoices):
        ESTUDIANTE = 'EST', _('Estudiante')
        EGRESADO = 'EGR', _('Egresado')

    class Categoria(models.TextChoices):
        PREGRADO = 'PRE', _('Pregrado')
        ESPECIALIZACION = 'ESP', _('Especializacion')
        MAESTRIA = 'MAE', _('Maestria')
        POSGRADO = 'POS', _('Posgrado')

    documento = models.CharField(max_length=15)
    nombre = models.CharField(max_length=70)
    email = models.EmailField()
    telefono = models.CharField(max_length=13)
    direccion = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=10, choices=Sexo.choices, null=True, blank=True)
    nacionalidad = models.CharField(max_length=30, null=True, blank=True)
    tipo = models.CharField(max_length=15, choices=Tipo.choices, null=True, blank=True)
    categoria = models.CharField(max_length=15, choices=Categoria.choices, null=True, blank=True)
    es_ofertante = models.BooleanField(default=False)
    es_administrador = models.BooleanField(default=False)


class HojaVida(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    descripcion = models.TextField()
    experiencia = models.FloatField(validators=[MinValueValidator(0)])
    otra_info = models.TextField()


class FormacionAcademica(models.Model):
    usuario = models.ForeignKey(Usuario, related_name='formacion_academica', on_delete=models.PROTECT)
    titulo = models.CharField(max_length=50)
    lugar = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    titulo_trabajo = models.TextField()


class FormacionComplementaria(models.Model):
    usuario = models.ForeignKey(Usuario, related_name='formacion_complementaria', on_delete=models.PROTECT)
    titulo = models.CharField(max_length=50)
    lugar = models.TextField()


class ExperienciaProfesional(models.Model):
    usuario = models.ForeignKey(Usuario, related_name='experiencia_profesional', on_delete=models.PROTECT)
    nombre_empresa = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    fecha_inicio =  models.DateField()
    fecha_fin = models.DateField()
    dedicacion_semanal = models.FloatField(validators=[MinValueValidator(0)])


class AreaActuacion(models.Model):
    usuario = models.ForeignKey(Usuario, related_name='area_actuacion', on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50)


class Idioma(models.Model):
    usuario = models.ForeignKey(Usuario, related_name='idioma', on_delete=models.PROTECT)
    nombre = models.CharField(max_length=15)
    habla = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    escribe = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    lee = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    escucha = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])


class Reconocimiento(models.Model):
    usuario = models.ForeignKey(Usuario, related_name='reconocimiento', on_delete=models.PROTECT)
    nombre = models.TextField()
    lugar = models.CharField(max_length=50)
    fecha = models.DateField()


class Publicacion(models.Model):
    usuario = models.ForeignKey(Usuario, related_name='publicacion', on_delete=models.PROTECT)
    nombre = models.TextField()
    titulo_publicacion = models.TextField()
    isbn = models.CharField(max_length=13, validators=[MinLengthValidator(10), MaxLengthValidator(13)])
    issn = models.CharField(max_length=8, validators=[MinLengthValidator(8), MaxLengthValidator(8)])
    editorial = models.CharField(max_length=50)


class Oferta(models.Model):
    class TipoContrato(models.TextChoices):
        INDEFINIDO = 'IND', _('Término Indefinido')
        FIJO = 'FIJ', _('Término Fijo')
        LABOR = 'LAB', _('Labor')
        OCASIONAL = 'OCA', _('Ocasional')
    nombre = models.CharField(max_length=15)
    fecha_limite = models.DateTimeField() # Default
    info_empresa = models.TextField()
    perfil = models.TextField()
    cant_vacantes = models.IntegerField(validators=[MinValueValidator(1)])
    observaciones = models.TextField()
    lugar_trabajo = models.CharField(max_length=100)
    conocimientos = models.TextField()
    experiencia = models.FloatField(validators=[MinValueValidator(0)])
    tipo_contrato = models.CharField(max_length=20, choices=TipoContrato.choices)
    contacto = models.CharField(max_length=50)
    remuneracion = models.FloatField(validators=[MinValueValidator(0)])
    informacion = models.TextField()
    funciones = models.TextField()

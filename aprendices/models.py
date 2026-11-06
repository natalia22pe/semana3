from django.db import models


class Programa(models.Model):
    nombre = models.CharField(max_length=23)
    ficha = models.IntegerField()
    programa = models.CharField(max_length=50)
    lugar = models.CharField(max_length=30)
    duracion = models.IntegerField()
    modalidad = models.CharField(max_length=20)
    nivel_profesional = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nombre} - Ficha: {self.ficha} ({self.programa})"


class Instructores(models.Model):
    nombre = models.CharField(max_length=23)
    apellido = models.CharField(max_length=23)
    documento = models.IntegerField(unique=True)
    especialidad = models.CharField(max_length=30)
    ficha_asignada = models.IntegerField()
    correo = models.EmailField(unique=True)
    telefono = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"


class Aprendiz(models.Model):
    nombre = models.CharField(max_length=23)
    apellido = models.CharField(max_length=23)
    documento = models.CharField(max_length=20, unique=True) 
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, unique=True)  
    ficha = models.CharField(max_length=20)                  
    programa = models.CharField(max_length=50)

    programa_rel = models.ForeignKey(
        Programa,
        on_delete=models.CASCADE,
        related_name="aprendices",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Doc: {self.documento}"


class Competencias(models.Model):
    nombre = models.CharField(max_length=23)
    ficha = models.IntegerField()
    instructor = models.CharField(max_length=23)

    programa_rel = models.ForeignKey(
        Programa,
        on_delete=models.CASCADE,
        related_name="competencias_programa",
        null=True,
        blank=True
    )

    instructores_rel = models.ForeignKey(
        Instructores,
        on_delete=models.CASCADE,
        related_name="competencias_instructores",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.nombre} - Ficha: {self.ficha}"
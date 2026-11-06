from django.contrib import admin
from .models import Aprendiz, Programa, Instructores, Competencias

admin.site.register(Programa)
admin.site.register(Instructores)
admin.site.register(Aprendiz)
admin.site.register(Competencias)
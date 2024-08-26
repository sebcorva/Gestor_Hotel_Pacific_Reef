from django.contrib import admin
from .models import habitaciones

class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_habitacion', 'descripcion', 'valor')
    search_fields = ('nombre_habitacion', 'descripcion')

admin.site.register(habitaciones, HabitacionAdmin)
from django.contrib import admin
from .models import Categoria

# Register your models here.
admin.site.register(Categoria)

class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('categoria_name',)}
    list_display = ('categoria_name', 'slug')
from django.contrib import admin
from .models import TipoServicio, Promocion, Servicio
# Register your models here.

# class TipoPromocionAdmin(admin.ModelAdmin):
#     readonly_fields = ("id",)

admin.site.register(Promocion)
admin.site.register(Servicio)
admin.site.register(TipoServicio)


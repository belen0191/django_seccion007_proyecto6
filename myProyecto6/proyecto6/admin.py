from django.contrib import admin
from .models import SliderIndex,ImagenGaleria,MisionyVision,Insumos
# Register your models here.

class SliderIndexAdmin(admin.ModelAdmin):
    list_display= ['ident','imagen']
    search_fields = ['ident']
    list_per_page = 10

class InsumosAdmin(admin.ModelAdmin):
    list_display= ['nombre','precio','descripcion','stock']
    search_fields = ['nombre','descripcion']
    list_per_page = 10

class ImagenGaleriaAdmin(admin.ModelAdmin):
    list_display= ['ident','imagen2']
    search_fields = ['ident']
    list_per_page = 10

class MisionyVisionAdmin(admin.ModelAdmin):
    list_display= ['ident','mision','vision']
    search_fields = ['ident','mision','vision']
    list_per_page = 10

admin.site.register(SliderIndex, SliderIndexAdmin)
admin.site.register(ImagenGaleria, ImagenGaleriaAdmin)
admin.site.register(MisionyVision, MisionyVisionAdmin)
admin.site.register(Insumos, InsumosAdmin)



from django.contrib import admin
from picture.models import Picture, Area


# Register your models here.
class PictureAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'path', 'create_date']
    list_per_page = 10


class AreaAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'parent']
    list_per_page = 10


admin.site.register(Picture, PictureAdmin)
admin.site.register(Area, AreaAdmin)
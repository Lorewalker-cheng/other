from django.contrib import admin
from second.models import Focus, Info


# Register your models here.
class FocusAdmin(admin.ModelAdmin):
    list_display = ['id', 'note_info', 'info_id']


class InfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'short', 'chg', 'turnover', 'price', 'highs', 'time']


admin.site.register(Focus, FocusAdmin)
admin.site.register(Info, InfoAdmin)
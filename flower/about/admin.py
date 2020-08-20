from django.contrib import admin
from .models import about
# Register your models here.
class aboutAdmin(admin.ModelAdmin):
    list_display = ('Description',)

admin.site.register(about,aboutAdmin)

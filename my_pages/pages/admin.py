from django.contrib import admin
from .models import Greeting

admin.site.register(Greeting)

class GreetingAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'created_at','email')
    search_fields = ('name', 'message','email')

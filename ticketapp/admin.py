from django.contrib import admin
from .models import Movie, Halls, Userdata

# Register your models here.\

admin.site.register(Movie)
admin.site.register(Halls)
admin.site.register(Userdata)

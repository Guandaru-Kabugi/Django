from django.contrib import admin
from .models import Blog,Entry,Author
# Register your models here.
admin.site.register(Blog)
admin.site.register(Entry)
admin.site.register(Author)
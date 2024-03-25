from django.contrib import admin
from .models import Post
# Registering models to appear on the admin page
admin.site.register(Post)
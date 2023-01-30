from django.contrib import admin
from .models import UserDetails
from .models import Products
from .models import Category

admin.site.register(UserDetails)
admin.site.register(Products)
admin.site.register(Category)

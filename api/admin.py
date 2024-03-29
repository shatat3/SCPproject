from django.contrib import admin

from .models import UsersModel, MealsModel

admin.site.register(UsersModel) 
admin.site.register(MealsModel)

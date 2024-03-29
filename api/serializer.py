from rest_framework.serializers import ModelSerializer
from .models import UsersModel, MealsModel
from rest_framework import serializers

class MealsSerializer(ModelSerializer):
    
    class Meta:
        model = MealsModel
        fields = '__all__'
        
class UserSerializer(ModelSerializer):
    meal=MealsSerializer()
    class Meta:
        model= UsersModel
        fields=['full_name','email','country','city','street','created','updated','meal',]
        


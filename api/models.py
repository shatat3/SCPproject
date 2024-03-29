from django.db import models

SOURCE_FOOD = [
("Home", 'Home'),
("Restaurant", 'Restaurant'),
("Other", 'Other')
]
FOOD_TYPE = [
    ('Veg','Veg'),
    ('NonVeg','NonVeg'),
    ('Both','Both'),
]
class MealsModel(models.Model):
    food_source = models.CharField(max_length=20, choices=SOURCE_FOOD, default='Home')
    restaurant =  models.CharField(max_length=200)
    food_type = models.CharField(max_length=20, choices=FOOD_TYPE, default='Veg')
    food_description = models.CharField(max_length=500)
    total_quantity = models.IntegerField(blank=True, null=True)
    image_food = models.ImageField(upload_to='imgs/')
    
    def __str__(self)->str:
        return self.restaurant
    

class UsersModel(models.Model):
    full_name=  models.CharField(max_length=70)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    country=models.CharField(max_length=40)
    city=models.CharField(max_length=40)
    street=models.CharField(max_length=100)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    meal = models.ForeignKey(MealsModel, on_delete=models.PROTECT,default=1)
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        ordering=['-updated']
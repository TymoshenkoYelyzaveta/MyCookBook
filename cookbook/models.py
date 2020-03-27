from django.db import models

# Create your models here.

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    time = models.CharField(max_length=20)
    instruction = models.TextField()


class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)


class RecipeIngredient(models.Model):
    id = models.AutoField(primary_key=True)
    id_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    id_ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.CharField(max_length=50)

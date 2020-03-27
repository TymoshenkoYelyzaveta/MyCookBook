from django import forms

from .models import Ingredient, Recipe

class IngredientForm(forms.ModelForm):
    name = forms.CharField(
                label='Ingredient name',
                widget=forms.TextInput(
                    attrs={'placeholder':'Enter Ingredient'}
                    )
                )

    class Meta:
        model = Ingredient
        fields = [
            'name'
        ]

class RecipeForm(forms.ModelForm):
    title = forms.CharField(label='Name of the recipe')
    image = forms.ImageField(label='Select an image')
    time = forms.CharField(label='How long does it take?')
    ingredients = forms.CharField(label='Ingredients', widget=forms.TextInput())
    instruction = forms.CharField(label='Steps', widget=forms.TextInput())

# foodwaste/recipes/forms.py
from django import forms

class RecipeForm(forms.Form):
    ingredients = forms.CharField(label='Ingredients', widget=forms.Textarea)
    dietary_preferences = forms.CharField(label='Dietary Preferences')


# foodwaste/recipes/forms.py
from django import forms

class PerishableItemForm(forms.Form):
    name = forms.CharField(label='Item Name')
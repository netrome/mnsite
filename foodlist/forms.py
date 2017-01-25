from django import forms
from .models import Dish


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ["name", "description", "time", "n_portions"]
        labels = {
            "name": "Maträtt",
            "description": "Beskrivning",
            "time": "Tillagningstid",
            "n_portions": "Antal portioner",
        }

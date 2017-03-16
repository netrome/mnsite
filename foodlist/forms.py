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

        widgets = {
            "name": forms.TextInput(attrs={"class": "w3-input"}),
            "description": forms.Textarea(attrs={"class": "w3-input"}),
            "time": forms.NumberInput(attrs={"class": "w3-input"}),
            "n_portions": forms.NumberInput(attrs={"class": "w3-input"}),
        }

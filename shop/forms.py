from django import forms
from .models import Plant

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'description', 'price', 'quantity', 'image']


class QuantityDeleteForm(forms.Form):
    quantity = forms.IntegerField(
        label="Quantity to Delete",
        min_value=1,
        help_text="Enter the number of plants to delete."
    )

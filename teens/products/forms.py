from django import forms

class QuantityForm(forms.Form):

    quantity = forms.IntegerField(required=True,  widget=forms.TextInput(
        attrs={'id':'quantity_input', 'value': 1}
    ))
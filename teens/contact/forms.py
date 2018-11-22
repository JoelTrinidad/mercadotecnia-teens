from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'review_form_input', 'placeholder': "Nombre"}
    ), min_length=3, max_length=100)
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class':'review_form_input', 'placeholder': "E-mail"}
    ), min_length=3, max_length=100)
    subject = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'review_form_input', 'placeholder': "Tema"}
    ), min_length=3, max_length=100)
    content = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class':'review_form_text', 'placeholder': "Mensaje"}
    ), min_length=10, max_length=1000)
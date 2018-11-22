from django import forms

class billingDetailsForm(forms.Form):
    firtsname = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'checkout_input checkout_input_50', 'placeholder':"Nombre"}
    ), min_length=2 ,max_length=100 )
    lastname = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'checkout_input checkout_input_50', 'placeholder':"Apellidos"}
    ), min_length=2 ,max_length=100 )
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class':'checkout_input', 'placeholder':"E-mail"}
    ), min_length=3, max_length=100)
    zipcode = forms.IntegerField(required=True, widget=forms.TextInput(
        attrs={'class':'checkout_input checkout_input_50', 'placeholder':"Codigo Postal"}
    ))
    town = forms.ChoiceField(choices=( ('','Delegación'),('c', 'Coyoacan'), ('t', 'Tlalpan'), ('x', 'Xochimilco') ), required=True, widget= forms.Select(
        attrs={'class':'country_select checkout_input'}
    ) )
    address = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'checkout_input', 'placeholder':"Dirección"}
    ), min_length=10 ,max_length=1000 )
    phonenum = forms.CharField( widget=forms.TextInput(
        attrs={'class':'checkout_input checkout_input_50', 'placeholder':"Telefono"}
    ), min_length=8 ,max_length=15)
    streetnumber = forms.IntegerField(required=True, widget=forms.TextInput(
        attrs={'class':'checkout_input checkout_input_50', 'placeholder':"Numero exterior"}
    ))
    unitnumber = forms.IntegerField(widget=forms.TextInput(
        attrs={'class':'checkout_input checkout_input_50', 'placeholder':"Numero interior"}
    ))
    comment = forms.CharField(widget=forms.Textarea(
        attrs={'class':'checkout_comment', 'id':'checkout_comment', 'name':'checkout_comment', 'placeholder': "Deje un comentario sobre su pedido"}
    ), min_length=10, max_length=1000)



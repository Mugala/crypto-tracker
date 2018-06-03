from django import forms
from .models import Profile,CryptocurrencyValue


class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')


class User_details (forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'bio', 'default_pic', ]
        exclude = ['email', ]

class UpdateOnCurrency (forms.ModelForm):
    class Meta:
        model = CryptocurrencyValue
        fields = ['currency', 'set_value', 'phone_number','message', ]
    
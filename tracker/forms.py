from django import forms
from .models import Profile


class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')


class Profile (forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', ]
        exclude = ['neighbourhood', ]



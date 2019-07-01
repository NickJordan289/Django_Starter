from django import forms
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=20)
    password = forms.CharField(label='password', max_length=30)


class RegisterForm(forms.Form):
    username = forms.CharField(label='username', max_length=20)
    password = forms.CharField(label='password', max_length=30)
    first_name = forms.CharField(label='first_name', max_length=30)
    last_name = forms.CharField(label='last_name', max_length=30)


#class ProposalForm(forms.ModelForm):
#    class Meta:
#        model = Proposal
#        fields = ('title', 'description', 'estimated_price', 'estimated_time',)
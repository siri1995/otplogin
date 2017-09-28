from django.forms import ModelForm, inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer, Address
from django import forms



class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ()


class AddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = ()

AddressFormSet = inlineformset_factory(Customer, Address,
                                               form=AddressForm, extra=1)



class SignUpForm(UserCreationForm):
    contact_number = forms.CharField(max_length=20)
    IAM_CHOICES = [
        ('agent', 'AGENT'),
        ('buyer', 'BUYER'),
        ('owner', 'OWNER'),
        ('builder', 'BUILDER'),
    ]

    iam_name = forms.CharField(label='What is your iam choice?', widget=forms.Select(choices=IAM_CHOICES))

    class Meta:
        model = User
        fields = ('username', 'email','contact_number','password1', 'password2',)










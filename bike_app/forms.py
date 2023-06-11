from django import forms
from django.contrib.auth.models import User
from .models import UserAccount
from .models import Complaint

# Form class
class AccountForm(forms.ModelForm):
    # form for password (not visible)
    password = forms.CharField(widget=forms.PasswordInput(), label="password")

    class Meta():
        # Uer
        model = User
        # Fields
        fields = ('username', 'email', 'password')
        # Name for fields
        labels = {'username': "username", 'email': "email"}


class AddAccountForm(forms.ModelForm):
    class Meta():
        # Model class
        model = UserAccount
        fields = ('name', 'surname',)
        labels = {'name': "name", 'surname': "surname", }


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('Descriptions',)
        widgets = {
            'Descriptions': forms.Textarea(attrs={'cols': 80, 'rows': 10, 'label': False}),
        }

class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['name', 'surname', 'balance']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.user.save()
            instance.save()
        return instance
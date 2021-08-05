from django import forms
from django.contrib.auth.models import User
from . import models


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['address', 'mobile', 'profile_pic']


class ProducerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class ProducerForm(forms.ModelForm):
    class Meta:
        model = models.Producer
        fields = ['address', 'mobile', 'profile_pic']


class DistributorUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class DistributorForm(forms.ModelForm):
    class Meta:
        model = models.Distributor
        fields = ['address', 'mobile', 'profile_pic']


class TheatreUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class TheatreForm(forms.ModelForm):
    class Meta:
        model = models.Theatre
        fields = ['address', 'mobile', 'profile_pic']


class SellToDistributorsForm(forms.Form):
    # to_field_name value will be stored when form is submitted.....__str__ method of customer model will be shown there in html
    distributor = forms.ModelChoiceField(queryset=models.Distributor.objects.filter(status=True),
                                         empty_label="Distributor Name", to_field_name='id')


class SellToTheatreForm(forms.Form):
    # to_field_name value will be stored when form is submitted.....__str__ method of customer model will be shown
    # there in html
    theatre = forms.ModelChoiceField(queryset=models.Theatre.objects.filter(status=True), empty_label="Theatre Name",
                                     to_field_name='id')
    price = forms.IntegerField()


class AdminTheatreForm(forms.Form):
    # to_field_name value will be stored when form is submitted.....__str__ method of customer model will be shown
    # there in html
    theatre = forms.ModelChoiceField(queryset=models.Theatre.objects.filter(status=True), empty_label="Theatre Name",
                                     to_field_name='id')


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.Feedback
        fields = ['by', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 6, 'cols': 30})
        }


# for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

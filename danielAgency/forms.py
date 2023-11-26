from django import forms
from django.contrib.auth.forms import UserCreationForm
import re
from datetime import date
from django.core.exceptions import ValidationError
from django.db.transaction import atomic

from danielAgency.models import Trip


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')



class TripModelForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        # Add any additional validation here if needed
        return cleaned_data


from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import atomic

from danielAgency.models import Profile


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    biography = forms.CharField(
        label='Tell us your story with movies', widget=forms.Textarea, min_length=20
    )

    @atomic
    def save(self, commit=True):
        self.instance.is_active = False
        result = super().save(commit)
        biography = self.cleaned_data['biography']
        profile = Profile(biography=biography, user=result)
        if commit:
            profile.save()
        return result




# booking
class BookingForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    number_of_persons = forms.IntegerField()


class ContactForm(forms.Form):
    name = forms.CharField(label="Name", required=True, max_length=128)
    email = forms.EmailField(label="Email", required=True)
    subject = forms.CharField(label="Subject", max_length=256)
    message = forms.CharField(label="Message", required=True, widget=forms.Textarea)


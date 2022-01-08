from django import forms
from bdaywishapp.models import Birthday


class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        fields = '__all__'




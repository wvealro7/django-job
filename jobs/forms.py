from django import forms

from .models import Applay

class ApplyModelForm(forms.ModelForm):
      class Meta:
            model = Applay
            fields = ['name','email','website','cv','cover_letter']

from django import forms

from .models import Applay,Job

class ApplyModelForm(forms.ModelForm):
      class Meta:
            model = Applay
            fields = ['name','email','website','cv','cover_letter']

class JobForm(forms.ModelForm):

      class Meta:
            model = Job
            fields = '__all__'
            exclude = ('slug','owner')
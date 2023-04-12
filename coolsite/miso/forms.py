from django import forms
from django.core.exceptions import ValidationError

from .models import *

class AddPostForm(forms.ModelForm):
     class Meta:
         model = Miso
         fields = '__all__'
from django import forms
from .models import *

class form_newProductDetail(forms.ModelForm):
	class Meta:
		model = newProductDetail
		fields = '__all__'




class form_oldProductDetail(forms.ModelForm):
	class Meta:
		model = oldProductDetail
		fields = '__all__'

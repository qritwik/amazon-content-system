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



class form_empDetail(forms.ModelForm):
	class Meta:
		model = empDetail
		fields = '__all__'



class form_oldDetailAmazon(forms.ModelForm):
	class Meta:
		model = oldDetailAmazon
		fields = '__all__'



class form_featureImage(forms.ModelForm):
	class Meta:
		model = featureImage
		fields = '__all__'

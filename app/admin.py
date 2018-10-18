from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib.auth.models import User, Group



# Register your models here.

admin.site.site_header = "Text Mercato ASIN Portal"
admin.site.site_title = "Text Mercato ASIN Portal"
admin.site.index_title = "Text Mercato ASIN Portal"
admin.site.unregister(User)
admin.site.unregister(Group)



admin.site.register(oldDetailAmazon)
admin.site.register(featureImage)


class asinDetailResource(resources.ModelResource):

    class Meta:
        model = asinDetail
        import_id_fields = ('asin',)
        fields = ('asin','status','email','extracted',)


@admin.register(asinDetail)
class asinForm(ImportExportModelAdmin):


	resource_class = asinDetailResource

	def name(self, instance):
		return instance.asin



class empDetailResource(resources.ModelResource):
	class Meta:
		model = empDetail


@admin.register(empDetail)
class empDetailForm(ImportExportModelAdmin):


	resource_class = empDetailResource

	def name(self, instance):
		return instance.email





class newProductDetailResource(resources.ModelResource):
	class Meta:
		model = newProductDetail


@admin.register(newProductDetail)
class UserproductForm(ImportExportModelAdmin):


	resource_class = newProductDetailResource

	def name(self, instance):
		return instance.title




class oldProductDetailResource(resources.ModelResource):
	class Meta:
		model = oldProductDetail


@admin.register(oldProductDetail)
class UserproductForm(ImportExportModelAdmin):


	resource_class = oldProductDetailResource

	def name(self, instance):
		return instance.title

from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources



# Register your models here.

admin.site.site_header = "Amazon ASIN System";


class newProductDetailResource(resources.ModelResource):
	class Meta:
		model = newProductDetail


@admin.register(newProductDetail)
class UserproductForm(ImportExportModelAdmin):


	resource_class = newProductDetailResource

	def name(self, instance):
		return instance.title


# class asinResource(resources.ModelResource):
# 	class Meta:
# 		model = asin
#
#
# @admin.register(asin)
# class UserasinForm(ImportExportModelAdmin):
#
#
#
# 	resource_class = asinResource
#
# 	def name(self, instance):
# 		return instance.asin



class oldProductDetailResource(resources.ModelResource):
	class Meta:
		model = oldProductDetail


@admin.register(oldProductDetail)
class UserproductForm(ImportExportModelAdmin):


	resource_class = oldProductDetailResource

	def name(self, instance):
		return instance.title

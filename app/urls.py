from django.conf.urls import url
from app import views

app_name = 'app'

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^detail/',views.detail,name="detail"),
    url(r'^manager/',views.manager,name="manager"),



]

from django.conf.urls import url
from app import views

app_name = 'app'

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^detail/',views.detail,name="detail"),
    url(r'^manager/',views.manager,name="manager"),
    url(r'^message/',views.message,name="message"),
    url(r'^fetch_asin',views.fetch_asin,name="fetch_asin"),
    url(r'^download_report',views.download_report,name="download_report"),
    url(r'^user/(?P<email>[\w\-\.\@\w]+)$',views.manager_user,name="manager_user"),




]

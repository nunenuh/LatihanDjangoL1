from django.conf.urls import url
from login import views

urlpatterns = [
    url(r'^$', views.LoginView.as_view(), name='view'),
    url(r'^proses/$', views.ProsesLoginView.as_view(), name='login'),
    url(r'^proses/logout$', views.ProsesLogoutView.as_view(), name='logout'),
]   
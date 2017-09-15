from django.conf.urls import url
from jurnal import views

urlpatterns = [
    url(r'^$', views.ListJurnalView.as_view(), name='view'),
    url(r'^tambah/$', views.TambahJurnalView.as_view(), name='tambah'),
    url(r'^simpan/$', views.SimpanJurnalView.as_view(), name='simpan'),
    url(r'^hapus/(?P<nomer>\d+)$', views.HapusJurnalView.as_view(), name='hapus'),
    url(r'^edit/(?P<nomer>\d+)$', views.EditJurnalView.as_view(), name='edit'),
    url(r'^update/$', views.EditJurnalView.as_view(), name='update'),
    
]   
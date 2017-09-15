from django.conf.urls import url
from transaksi import views

urlpatterns = [
    url(r'^(?P<jurnal_id>\d+)/view$', views.ListTransaksiView.as_view(), name='view'),
    
    url(r'^(?P<jurnal_id>\d+)/simpan/$', views.SimpanTransaksiView.as_view(), name='simpan'),
    # url(r'^hapus/(?P<nomer>\d+)$', views.HapusJurnalView.as_view(), name='hapus'),
    # url(r'^edit/(?P<nomer>\d+)$', views.EditJurnalView.as_view(), name='edit'),
    # url(r'^update/$', views.EditJurnalView.as_view(), name='update'),
    
]   
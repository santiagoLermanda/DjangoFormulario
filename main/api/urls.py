from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^suscriptores/$',
		views.SuscriptorListView.as_view(),
		name="suscriptor_list"),

	url(r'^suscriptores/(?P<pk>\d+)/$',
		views.SuscriptorDetailView.as_view(),
		name="suscriptor_detail"),

	url(r'^suscriptores/crear/$',
		views.SuscriptorCreateView.as_view(),
		name="suscriptor_crear"),
]
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',  views.index_view),
    url(r'^control/$',  views.control_view),
    url(r'^property/$',  views.property_view),
    url(r'^login/$',views.authentication, name='authentication'),
    url(r'^logout/$',views.logout_view, name='logout'),
]
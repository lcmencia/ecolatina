# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^$', views.send_email, name='home'),
    url(r'^blog/$',  views.blog_list, name='blog_list'),
    url(r'^blog/(?P<slug>[-\w]+)/$',  views.blog_detail, name='blog_detail'),
    url(r'^panel/$',  views.index_view, name='panel'),
    url(r'^all_control/$',  views.all_control_view, name='all_control'),
    url(r'^control/(?P<id>\d+)/$',  views.control_view, name='control'),
    url(r'^property/$',  views.property_view, name='property'),
    url(r'^sector/(?P<id>\d+)/$',  views.sector_view, name='sector'),
    url(r'^station/(?P<id>\d+)/$',  views.station_view, name='station'),
    url(r'^login/$',views.authentication, name='authentication'),
    url(r'^logout/$',views.logout_view, name='logout'),
    url(r'^api/chart/data/$', views.ChartData.as_view()),
    url(r'^reporte_excel/$', views.ReporteExcel,
        name="reporte_excel")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


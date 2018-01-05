from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^panel/$',  views.index_view),
    url(r'^control/$',  views.control_view),
    url(r'^property/$',  views.property_view),
    url(r'^login/$',views.authentication, name='authentication'),
    url(r'^logout/$',views.logout_view, name='logout'),
    
    url(r'^api/chart/data/$', views.ChartData.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


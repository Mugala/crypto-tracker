from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('^$', views.welcome, name='welcome'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^crypto/', views.crypto, name='crypto'),
    url(r'^news/', views.news, name='news'),
    url(r'^accounts/profile/', views.user_profile, name='user_profile'),
    url(r'^accounts/my_profile/', views.my_profile, name='my_profile'),
    url(r'^accounts/notification/', views.notification, name='notification'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

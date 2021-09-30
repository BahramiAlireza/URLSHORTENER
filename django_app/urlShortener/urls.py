from django.contrib import admin
from django.urls import path

from shortener import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.url_create),
    path('u/<str:shorten_url>/', views.url_update_delete_retrieve),
]
    # path('u/<str:shorten>/', views.UrlCrudRoutes),

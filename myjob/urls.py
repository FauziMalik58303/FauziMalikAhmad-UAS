# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from myjob import views


from myjob.authentication import login, logout, registrasi
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),


    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('berita-bola/', views.berita_bola, name='berita_bola'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('artikel/<int:id>/', views.artikel_detail, name='artikel_detail'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/artikel_list', views.artikel_list, name='artikel_list'),

    path('dashboard/', include("artikel.urls")),
    path('api/', include("artikel.urls_api")),

#############################Authentication###############
    path('auth_login', login, name='login'),
    path('auth_logout', login, name='logout'),
    path('registrasi', registrasi, name='registrasi'),

]

# Menambahkan pengaturan untuk melayani file media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
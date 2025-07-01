from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from myjob import views
from myjob.authentication import login, logout, registrasi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # Halaman umum
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('berita-bola/', views.berita_bola, name='berita_bola'),

    # Artikel
    path('artikel/<int:id>/', views.artikel_detail, name='artikel_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/artikel_list', views.artikel_list, name='artikel_list'),
    path('dashboard/', include("artikel.urls")),

    # API
    path('api/', include("artikel.urls_api")),

    # Authentication (custom)
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('registrasi/', registrasi, name='registrasi'),

    # CKEditor
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]

# File media saat debug
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

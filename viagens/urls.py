from django.contrib import admin
from django.urls import include, path


    # path('',views_home.home),
    # path('home/',views_home.home),
    
urlpatterns = [
    path('',include('home.urls')),
    path('home/',include('home.urls')),
    path('blog/',include('blog.urls')),
    path('pacotes/',include('pacotes.urls')),
    path('fotos/',include('fotos.urls')),
    path('cadastro/',include('cadastro.urls')),
    path('admin/', admin.site.urls),
]

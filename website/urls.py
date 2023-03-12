from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('product', views.product, name='product'),
    path('furniture', views.furniture, name='furniture'),
    path('application', views.application, name='application'),
    path('timber', views.timber, name='timber')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

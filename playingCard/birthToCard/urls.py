from django.urls import path
from . import views
from django.conf.urls import static
from django.conf import settings
urlpatterns = [
    path('', views.getDate, name= 'getdate'),
] + static.static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)

urlpatterns += static.static(settings.B2C_CSS_URL, document_root= settings.B2C_CSS_ROOT)

from django.urls import path, include
from .views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('students/', include('students.urls')),
    path('faculty/', include('faculty.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

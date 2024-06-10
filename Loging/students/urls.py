from django.urls import path, include
from .views import student_id, download
from django.conf import settings
from django.conf.urls.static import static

app_name = 'students'

urlpatterns = [
                  path('<int:students_id>/', student_id, name='students'),
                  path('download/<int:students_id>/', download, name='download')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

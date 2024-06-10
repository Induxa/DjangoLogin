from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authorization.urls')),
    path('student/', include('students.urls', namespace='students')),
    path('faculty/', include('faculty.urls', namespace='faculty')),
]

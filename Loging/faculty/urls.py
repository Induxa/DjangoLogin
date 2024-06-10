from django.urls import path
from .views import faculty_index, logoutUser, Parsing, archive, Report, download_file, graph, Working, faculty_students, \
    transfer
# from .views import faculty_index, logoutUser, Parsing, faculty_students, download_file, transfer, graph
from django.conf import settings
from django.conf.urls.static import static

app_name = 'faculty'

urlpatterns = [
                  path('<int:faculty_id>', faculty_index, name='faculty_index'),
                  path('archive/<int:faculty_id>/', archive, name='archive'),
                  path('faculty_students/<int:faculty_id>/', faculty_students, name='faculty_students'),
                  path('parsing/<int:faculty_id>/', Parsing, name='parsing'),
                  path('Report/<int:faculty_id>/', Report, name='Report'),
                  path('Work/<int:faculty_id>/<slug:students_id>/', Working, name='Work'),
                  path('logout/', logoutUser, name='logout'),
                  path('download', download_file, name='download'),
                  path('transfer/<int:faculty_id>/', transfer, name='transfer'),
                  path('graph/<int:faculty_id>/', graph, name='graph'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

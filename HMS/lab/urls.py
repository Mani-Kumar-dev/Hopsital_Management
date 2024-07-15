from django.urls import path
from .views import labtest_list, add_lab_test, update_lab_test, delete_lab_test
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    path('', labtest_list, name='labtest_list'),
    path('add/', add_lab_test, name='add_lab_test'),
    path('update/<int:pk>/', update_lab_test, name='update_lab_test'),
    path('delete/<int:pk>/', delete_lab_test, name='delete_lab_test'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

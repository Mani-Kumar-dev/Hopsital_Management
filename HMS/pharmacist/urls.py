from django.urls import path
from .views import pharmacist_list, add_medicine, update_medicine, delete_medicine
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', pharmacist_list, name='pharmacist_list'),
    path('add/',add_medicine, name='add_medicine'),
    path('update/<int:pk>/', update_medicine, name='update_medicine'),
    path('delete/<int:pk>/', delete_medicine, name='delete_medicine'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),
    path('<int:pk>/', views.doctor_detail, name='doctor_detail'),
    path('add/', views.add_doctor, name='add_doctor'),
    path('<int:pk>/edit/', views.edit_doctor, name='edit_doctor'),  
    path('<int:pk>/delete/', views.doctor_delete, name='delete_doctor'),   
    path('<int:pk>/form/', views.doctor_form, name='doctor_form'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




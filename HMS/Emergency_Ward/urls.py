from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('create_patient/', views.patient_create, name='patient_create'),
    path('patient_detail/', views.patient_detail, name='patient_detail'),
    path('patient/<int:pk>/update/', views.patient_update, name='patient_update'),
    path('patient/<int:pk>/delete/', views.patient_delete, name='patient_delete'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

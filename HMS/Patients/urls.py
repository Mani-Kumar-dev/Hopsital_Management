from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('register',view=patient_register,name='patient_register'),
    path('',view=patientDashboard,name='patient_dashboard'),
    path('admission', view=patient_admission, name='patientAdmission'),
]

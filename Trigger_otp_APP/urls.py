from django.urls import path
from . import views

urlpatterns = [
    path('', views.TriggerOtp.as_view(), name='send_ot_views'),
]

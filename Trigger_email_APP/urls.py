from django.urls import path
from . import views

urlpatterns = [
    path('', views.TriggerEmail.as_view(), name='send_email_views'),
]

from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.TranslatorViews.as_view())
]

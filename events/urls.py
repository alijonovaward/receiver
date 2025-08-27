from django.urls import path
from .views import receive_event

urlpatterns = [
    path('', receive_event, name='receive_event'),
]

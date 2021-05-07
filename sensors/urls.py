
from django.urls import path
from .views import Sensors

urlpatterns = [
    path('sensors/', Sensors.as_view()),
]

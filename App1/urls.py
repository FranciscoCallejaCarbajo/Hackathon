from django.urls import path
from App1.views import IndexView

urlpatterns = [
    path('', IndexView)
]

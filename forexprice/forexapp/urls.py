from django.urls import path
from .views import get_xrt_data

urlpatterns = [
    path('api/xrt_data/', get_xrt_data, name='get_xrt_data'),
]

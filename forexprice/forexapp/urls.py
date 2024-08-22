from django.urls import path
from .views import get_xrt_data

urlpatterns = [
    path('api/xrt_data/', get_xrt_data, name='get_xrt_data'),
    path('', get_xrt_data, name='home'),  # Root URL points to `get_xrt_data`
]
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('api/v1/register/', RegistrationView.as_view({'post': 'create'})),
    path('api/v1/feedback/', FeedbackView.as_view({'post': 'create'})),
]
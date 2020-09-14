from django.urls import path
from .views import SignUpView


urlpatterns = [
    
    path('', SignUpView.as_view(), name='signup'),
    path('', SignUpView.as_view(), name='password_reset'),
]

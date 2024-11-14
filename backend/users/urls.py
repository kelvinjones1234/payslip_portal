from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
# from .views import (
#   MyTokenObtainPairView, 
#   SendOTPView, VerifyOTPView

 

# )
# from .views import RegisterUserView
# urlpatterns = [
#   path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
#   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#   path('register/', RegisterUserView.as_view(), name='register'),
#   path('send-otp/', SendOTPView.as_view(), name='send_otp'),
#   path('verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
#   # path('password-reset/', PasswordResetRequestView.as_view(), name='password_reset_request'),
#   # path('reset-password/<uidb64>/<token>/', PasswordResetView.as_view(), name='password_reset_confirm'),

# ]


# urls.py
from django.urls import path
from .views import InitiateLoginView, VerifyOTPView

urlpatterns = [
    path('login/initiate/', InitiateLoginView.as_view(), name='initiate-login'),
    path('login/verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
]
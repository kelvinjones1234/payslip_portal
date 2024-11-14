# from django.shortcuts import render
# from rest_framework_simplejwt.views import TokenObtainPairView
from.serializers import (
    MyTokenObtainPairSerializer, 
    # UserSerializer,
    )

from rest_framework.permissions import AllowAny
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework import generics, status
from .models import User
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response

# from django.core.mail import send_mail
# from django.core.cache import cache
# import random

# from rest_framework.views import APIView


# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer


# class RegisterUserView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     permission_classes = [AllowAny]
#     serializer_class = UserSerializer


# # class SendOTPView(APIView):
# #     def post(self, request):
# #         email = request.data.get('email')
# #         otp = str(random.randint(100000, 999999))  # Generate 6-digit OTP
        
# #         # Store OTP in cache for 5 minutes (300 seconds)
# #         cache.set(f'otp_{email}', otp, timeout=300)
        
# #         # Send OTP to user's email
# #         send_mail(
# #             'Your Login OTP',
# #             f'Your OTP is {otp}',
# #             'from@example.com',  # Replace with a valid email sender
# #             [email],
# #             fail_silently=False,
# #         )
# #         return Response({"message": "OTP sent successfully."}, status=status.HTTP_200_OK)


# class SendOTPView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         otp = str(random.randint(100000, 999999))  # Generate 6-digit OTP
        
#         # Store OTP in cache for 5 minutes (300 seconds)
#         cache.set(f'otp_{email}', otp, timeout=300)
        
#         # Print OTP to console instead of sending it to email
#         print(f"OTP for {email}: {otp}")
        
#         return Response({"message": "OTP generated successfully (check console for OTP)."}, status=status.HTTP_200_OK)



# class VerifyOTPView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         otp = request.data.get('otp')

#         # Retrieve OTP from cache
#         cached_otp = cache.get(f'otp_{email}')
        
#         if cached_otp == otp:
#             # Clear OTP from cache after successful validation
#             cache.delete(f'otp_{email}')
            
#             # Generate JWT token for the user
#             try:
#                 user = User.objects.get(email=email)
#                 refresh = RefreshToken.for_user(user)
#                 return Response({
#                     'refresh': str(refresh),
#                     'access': str(refresh.access_token),
#                 })
#             except User.DoesNotExist:
#                 return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             return Response({"error": "Invalid or expired OTP."}, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from .utils import OTPUtil
from .serializers import LoginSerializer, OTPVerificationSerializer

class InitiateLoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                ippis_number=serializer.validated_data['ippis_number'],
                password=serializer.validated_data['password']
            )
            
            if user is not None:
                # Generate OTP
                otp_code = OTPUtil.generate_otp(user)
                
                # Send OTP via HTML email
                subject = 'Security Verification Code - FPB Payslip Portal'
                html_message = f"""
                <html>
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    </head>
                    <body style="font-family: 'Segoe UI', Arial, sans-serif; background-color: #f6f9fc; margin: 0; padding: 0;">
                        <div style="max-width: 600px; margin: 40px auto; background-color: #ffffff; padding: 40px; border-radius: 12px; box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.05);">
                            <!-- Header with Logo -->
                            <div style="text-align: center; margin-bottom: 30px;">
                                <h1 style="color: #1a3353; margin: 0; font-size: 24px; font-weight: 600;">FPB Payslip Portal</h1>
                            </div>
                            
                            <!-- Main Content -->
                            <div style="margin-bottom: 30px;">
                                <p style="font-size: 16px; color: #1a3353; margin-bottom: 20px;">
                                    Dear {user.full_name},
                                </p>
                                <p style="font-size: 16px; color: #4a5568; line-height: 1.6;">
                                    A login attempt was made to your FPB Payslip Portal account. To complete the authentication process, please use the following verification code:
                                </p>
                                
                                <!-- OTP Code Box -->
                                <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 30px 0; text-align: center;">
                                    <div style="font-size: 32px; font-weight: 600; color: #2d3748; letter-spacing: 4px;">
                                        {otp_code}
                                    </div>
                                    <p style="font-size: 14px; color: #718096; margin-top: 10px;">
                                        This code will expire in 5 minutes
                                    </p>
                                </div>
                            </div>
                            
                            <!-- Security Notice -->
                            <div style="background-color: #fff8f1; border-left: 4px solid #ed8936; padding: 15px; margin-bottom: 30px;">
                                <p style="font-size: 14px; color: #744210; margin: 0;">
                                    If you didn't attempt to log in, please secure your account by changing your password immediately and contact our support team.
                                </p>
                            </div>
                            
                            <!-- Footer -->
                            <div style="border-top: 1px solid #e2e8f0; padding-top: 20px; margin-top: 30px;">
                                <p style="font-size: 14px; color: #718096; margin: 0; text-align: center;">
                                    This is an automated message, please do not reply to this email.<br>
                                    © 2024 FPB Payslip Portal. All rights reserved.
                                </p>
                            </div>
                        </div>
                    </body>
                </html>
                """
                plain_message = f"Your verification code for FPB Payslip Portal is: {otp_code}. This code will expire in 5 minutes."
                from_email = f'FPB Payslip Portal <{settings.DEFAULT_FROM_EMAIL}>'
                recipient_list = [user.email]

                try:
                    send_mail(
                        subject,
                        plain_message,
                        from_email,
                        recipient_list,
                        fail_silently=False,
                        html_message=html_message
                    )
                except Exception as e:
                    return Response({
                        'error': 'Failed to send verification code.',
                        'details': str(e)
                    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                return Response({
                    'message': 'A verification code has been sent to your email.',
                    'ippis_number': user.ippis_number
                })
            
            return Response({
                'error': 'Invalid credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyOTPView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = OTPVerificationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(ippis_number=serializer.validated_data['ippis_number'])
                
                if OTPUtil.verify_otp(user, serializer.validated_data['otp_code']):
                    # Generate JWT token
                    refresh = MyTokenObtainPairSerializer.get_token(user)
                    
                    return Response({
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    })
                    
                return Response({
                    'error': 'Invalid or expired verification code'
                }, status=status.HTTP_400_BAD_REQUEST)
                
            except User.DoesNotExist:
                return Response({
                    'error': 'Invalid user'
                }, status=status.HTTP_400_BAD_REQUEST)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
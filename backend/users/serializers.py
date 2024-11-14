from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework import serializers
# from .models import User




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
      token = super().get_token(user)
      token['email'] = user.email
      token['phone'] = user.phone
      token['ippis_number'] = user.ippis_number
      token['level'] = user.level
      token['department'] = user.department.name
      token['full_name'] = user.full_name


      return token


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('email', 'phone', 'full_name', 'ippis_number', 'gender', 'title', 'level', 'department', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             email=validated_data['email'],
#             full_name=validated_data['full_name'],
#             ippis_number=validated_data['ippis_number'],
#             gender=validated_data['gender'],
#             title=validated_data['title'],
#             level=validated_data['level'],
#             phone=validated_data['phone'],
#             department=validated_data['department'],
#             password=validated_data['password'],
#         )
#         return user


from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    ippis_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

class OTPVerificationSerializer(serializers.Serializer):
    ippis_number = serializers.CharField()
    otp_code = serializers.CharField()
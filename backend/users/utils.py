from django.core.cache import cache
import random

class OTPUtil:
    OTP_EXPIRATION_TIME = 300  # seconds

    @staticmethod
    def generate_otp(user):
        otp_code = random.randint(100000, 999999)
        cache.set(f'otp_{user.id}', otp_code, timeout=OTPUtil.OTP_EXPIRATION_TIME)
        return otp_code

    @staticmethod
    def verify_otp(user, otp_code):
        # Retrieve the OTP from cache
        cached_otp = cache.get(f'otp_{user.id}')
        
        # Verify and immediately delete the OTP if it matches
        if str(cached_otp) == str(otp_code):
            cache.delete(f'otp_{user.id}')  # Expire the OTP after use
            return True
        return False


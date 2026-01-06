from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError


class AuthService:
    @staticmethod
    def logout(refresh_token: str) -> None:
        """
        Refresh tokenni blacklist qilish
        """
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            raise ValidationError({'refresh': 'Invalid or expired token'})


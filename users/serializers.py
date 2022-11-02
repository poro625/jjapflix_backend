from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


VALID_EMAIL_LIST = ["naver.com", "gmail.com", "daum.net"]



class UserProfileSerializer(serializers.ModelSerializer):  # 프로필 조회
    class Meta:
        model = User
        fields="__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
    def validate(self, data):
        if data.get("email", "").split('@')[-1] not in VALID_EMAIL_LIST:
            raise serializers.ValidationError(
                detail={"error": "naver, gmail, daum 이메일 주소만 사용 가능합니다."}
            )
        return data    
    
    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password) # 패스워드 해싱
        user.save()
        return user


    def update(self, validated_data):
        user = super().update(validated_data)
        password = user.password
        user.set_password(password) # 패스워드 해싱
        user.save()
        return user 

        
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):   # jwt payload 커스텀
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email

        return token
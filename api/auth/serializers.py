from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainpair_Serializer(TokenObtainPairSerializer):
    @classmethod

    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['staff_category'] = user.staff_category
        token['username'] = user.username

        return token
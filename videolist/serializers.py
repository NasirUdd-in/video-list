from rest_framework import serializers
from .models import CustomUser,Movie, Rating
from rest_framework import serializers



class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Include password field for input only

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone', 'password']


class MovieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['name', 'genre', 'release_date']



class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'user', 'movie', 'rating']
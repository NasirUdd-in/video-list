from .models import CustomUser, Rating
from .serializers import CustomUserSerializer,UserLoginSerializer,MovieCreateSerializer,RatingSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from rest_framework import generics



class UserLoginAPIView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)
            if user:
                # User is authenticated, perform further actions (e.g., generate token)
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserAPIView(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MovieCreateAPIView(APIView):
    def post(self, request):
        serializer = MovieCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RatingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Rating
from django.db.models import Avg

class AllRatings(APIView):
    def get(self, request):
        # Retrieve all unique movies along with their average ratings
        unique_movies_with_avg = Rating.objects.values('movie__id', 'movie__name', 'movie__genre', 'movie__release_date').annotate(average_rating=Avg('rating'))

        if not unique_movies_with_avg:
            return Response({"message": "No movies found with ratings"}, status=status.HTTP_404_NOT_FOUND)

        # Construct response data
        response_data = []
        for movie in unique_movies_with_avg:
            response_data.append({
                "id": movie['movie__id'],
                "name": movie['movie__name'],
                "genre": movie['movie__genre'],
                "rating": movie['average_rating'],
                "relase_date": movie['movie__release_date'],
            })

        return Response(response_data, status=status.HTTP_200_OK)
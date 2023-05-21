from rest_framework import views 
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from models import Author, Audio, Summary, SummaryGender
from serializers import AuthorSerializer, Author, SummarySerializer, SummaryGenderSerializer
from setup.permission import OnlyAdminCanPost


class AuthorViewSet(views.APIView):
    pass


class AudioViewSet(views.APIView):
    permission_classes = [OnlyAdminCanPost]
     
    def post(self, request, format=None):
        serializer = AudioSerializer(data=serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.erros, status=400)
    
    def get(self, request, audio_name):
        queryset = Audio.objects.get(audio_name=audio_name)
        serializer = AudioSerializer(queryset)
        return Response(serializer.data, status=200)


class SummariesViewSet(views.APIView):
    permission_classes = [OnlyAdminCanPost]

    def post(self, request):
        serializer = SummaryGenderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def get(self, request):
        queryset = SummaryGender.objects.all()
        serializer = SummaryGenderSerializer(queryset, many=True)
        return Response(serializer, status=200)


class SummaryViewSet(views.APIView):
    def get(self, request, id):
        queryset = SummaryGender.objects.get(id=id)
        serializer = SummaryGenderSerializer(queryset)
        return Response(serializer, status=200)


class SummaryGenderViewSet(views.APIView):
    permission_classes = [OnlyAdminCanPost]

    def post(self, request):
        serializer = SummaryGenderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def get(self, request):
        queryset = SummaryGender.objects.all()
        serializer = SummaryGenderSerializer(queryset, many=True)
        return Response(serializer, status=200)
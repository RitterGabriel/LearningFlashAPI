from rest_framework import views 
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.http import FileResponse
from setup.permission import OnlyAdminCanPost
from .models import Author, Audio, Summary, SummaryGender
from .serializers import AuthorSerializer, Author, SummarySerializer, SummaryGenderSerializer, AudioSerializer


class AuthorViewSet(views.APIView):
    permission_classes = [OnlyAdminCanPost]

    def get(self, request):
        queryset = Author.objects.all().order_by('id')
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AudioViewSet(views.APIView):
    permission_classes = [OnlyAdminCanPost]
    parser_classes = [FileUploadParser]
     
    def post(self, request, phrase):
        data = {
            'audio_name': phrase,
            'audio_content': request.FILES['file']
        }
        serializer = AudioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request, phrase):
        queryset = Audio.objects.get(audio_name=phrase)
        print(queryset.audio_content)
        response = FileResponse(queryset.audio_content.open(), content_type='audio/mpeg')
        response['Content-Disposition'] = f'attachment; filename="{queryset.audio_content.name}"'
        return response


class SummariesViewSet(views.APIView):
    permission_classes = [OnlyAdminCanPost]

    def post(self, request):
        serializer = SummarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def get(self, request):
        queryset = Summary.objects.all()
        serializer = SummarySerializer(queryset, many=True)
        return Response(serializer.data, status=200)


class SummaryViewSet(views.APIView):
    def get(self, request, id):
        queryset = Summary.objects.get(id=id)
        serializer = SummarySerializer(queryset)
        return Response(serializer.data, status=200)


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
        return Response(serializer.data, status=200)
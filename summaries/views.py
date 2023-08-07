from rest_framework import views 
from rest_framework.response import Response
from setup.permission import OnlyAdminCanPost
from summaries.models import (
    Author, 
    Summary,
    SummaryGender, 
    Phrase
)
from summaries.serializers import (
    AuthorSerializer,
    SummarySerializer,
    SummariesSerializer, 
    CreateSummarySerializer, 
    SummaryGenderSerializer, 
)


class AuthorsView(views.APIView):
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


class SummariesView(views.APIView):
    permission_classes = [OnlyAdminCanPost]

    def post(self, request):
        serializer = CreateSummarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def get(self, request):

        query_filter = request.GET.get('filter')
        if query_filter is None:
            query_filter = ''
        else:
            query_filter = ''.join(query_filter.lower().split())

        sql = """
            SELECT * FROM public.summaries_summary
            WHERE LOWER(REPLACE(title, ' ', '')) LIKE %s 
        """

        queryset = Summary.objects.raw(sql, params=[f'%{query_filter}%'])
        serializer = SummariesSerializer(queryset, many=True)
        return Response(serializer.data, status=200)


class SummaryView(views.APIView):
    def get(self, request, id):
        queryset = Summary.objects.get(id=id)
        serializer = SummarySerializer(queryset)
        return Response(serializer.data, status=200)


class SummaryGenderView(views.APIView):
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


class PhraseView(views.APIView):
    def get(self, request, phrase):
        sql = """
            SELECT * FROM public.summaries_phrase
            WHERE LOWER(phrase) = %s 
        """
        phrases = Phrase.objects.raw(sql, [phrase.lower()])
        if phrases:
            phrase_obj, = phrases
            data = {
                'phrase': phrase_obj.phrase,
                'translated_phrase': phrase_obj.translated_phrase,
            }
            return Response(data, status=200)
        return Response({'message': 'there\'s no translation for this phrase'}, status=404)

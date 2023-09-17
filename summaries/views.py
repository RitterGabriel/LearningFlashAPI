from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from setup.permission import OnlyAdminCanPost
from summaries.models import (
    Author, 
    Summary,
    SummaryGender, 
    Phrase,
    Favorite,
)
from summaries.serializers import (
    AuthorSerializer,
    SummarySerializer,
    SummariesSerializer,
    CreateSummarySerializer, 
    SummaryGenderSerializer,
    FavoriteSerializer,
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
            ORDER BY id DESC
        """

        queryset = Summary.objects.raw(sql, params=[f'%{query_filter}%'])
        serializer = SummariesSerializer(queryset, many=True)
        return Response(serializer.data, status=200)


class SummaryView(views.APIView):
    def get(self, request, id):
        query_result = self._fetch_summary(request.user.id, id)
        if not query_result:
            return Response({'mensagem': 'Não há nenhum livro com o id informado'}, status=404)
        summary_data, = query_result
        serializer = SummarySerializer(summary_data)
        return Response(serializer.data, status=200)

    def _fetch_summary(self, user_id, book_id):
        sql = """
            SELECT summaries_summary.id, title, text_content, author_name,
            (SELECT count(*) = 1 FROM summaries_favorite WHERE user_id = %s AND summary_id = %s) as is_favorite
            FROM public.summaries_summary
            LEFT JOIN summaries_favorite
            ON summaries_summary.id = summaries_favorite.summary_id
            INNER JOIN summaries_author
            ON summaries_summary.author_id = summaries_author.id
            WHERE summaries_summary.id = %s
            LIMIT 1
        """
        query_result = Summary.objects.raw(sql, [user_id, book_id, book_id])
        return tuple(query_result)


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


class FavoritesView(views.APIView):
    permission_classes = IsAuthenticated,

    def get(self, request):
        favorites = Favorite.objects.select_related('summary').filter(user=request.user.id)
        serializer = SummariesSerializer([favorite.summary for favorite in favorites], many=True)
        return Response(serializer.data)

    def post(self, request):
        request.data['user'] = request.user.id
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request):
        user_id = request.user.id
        favorite_record = Favorite.objects.filter(summary=request.data['summary'], user=user_id)
        favorite_record.delete()
        return Response({'status': 'deletado com sucesso'}, status=200)

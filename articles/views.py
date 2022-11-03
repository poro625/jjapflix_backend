from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from django.db.models.query_utils import Q
from articles import serializers
from articles.models import Comment,Movie
from articles.serializers import ArticleSerializer,ArticleListSerializer,MovieSerializer, ArticleDetailSerializer



class ArticlesView(APIView):  #영화리스트(노우석님)
    def get(self, request):
        articles = Comment.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArticlesDetailView(APIView): #영화상세보기(양기철님)
    def get(self, request, movie_id):
        movie = Movie.objects.get(id=movie_id)
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = ArticleDetailSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArticlesMovieLikeView(APIView):#영화좋아요(성창남님)
    
    def post(self, request):
        pass 
class ArticlesCommentView(APIView): #영화리뷰(작성,수정,삭제)(노우석님)

    def post(self, request,movie_id):

        article = Movie.objects.get(id=movie_id)
        comments = article.comment_set.all()
        serializer = MovieSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request):
        pass   


    def delete(self, request):
        pass


class ArticlesCommentLikeView(APIView): #영화리뷰좋아요(성창남님)

    def post(self, request):
        pass



class ArticlesSearchView(APIView): #검색(양기철님)
    # queryset = Movie.objects.all()
    # serializer_class = ArticleSerializer

    # filter_backends = [SearchFilter]
    # # 검색 키워드를 지정했을 때, 매칭을 시도할 필드
    # search_fields = ['title', 'description', 'category']
    def get(self, request):
        pass

    def post(self, request):
        pass
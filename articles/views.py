from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from django.db.models.query_utils import Q
from articles import serializers
from articles.models import Comment,Movie
from articles.serializers import ArticleSerializer


class ArticlesView(APIView):  #영화리스트
    def get(self, request):
        pass


class ArticlesDetailView(APIView): #영화상세보기
    def get(self, request):
        pass


class ArticlesMovieLikeView(APIView): #영화좋아요
    def post(self, request):
        pass


class ArticlesCommentView(APIView): #영화리뷰(작성,수정,삭제)

    def post(self, request):
        pass


    def put(self, request):
        pass   


    def delete(self, request):
        pass


class ArticlesCommentLikeView(APIView): #영화리뷰좋아요

    def post(self, request):
        pass



class ArticlesSearchView(APIView): #검색


    def get(self, request):
        pass

    def post(self, request):
        pass
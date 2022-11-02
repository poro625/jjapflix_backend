from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from django.db.models.query_utils import Q
from articles import serializers
from articles.models import Article,Comment
from articles.serializers import ArticleSerializer


class ArticlesView(APIView):
    def get(self, request):
        pass


class ArticlesDetailView(APIView):
    def get(self, request):
        pass


class ArticlesMovieLikeView(APIView):
    def post(self, request):
        pass


class ArticlesCommentView(APIView):

    def post(self, request):
        pass


    def put(self, request):
        pass   


    def delete(self, request):
        pass


class ArticlesCommentLikeView(APIView):

    def post(self, request):
        pass

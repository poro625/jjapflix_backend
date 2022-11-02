from rest_framework import serializers

from articles.models import Movie,Comment


class ArticleSerializer(serializers.ModelSerializer):


    class Meta:
        model = Comment
        fields='__all__'

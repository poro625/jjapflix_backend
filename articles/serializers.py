from rest_framework import serializers

from articles.models import Movie,Comment

class ArticleSerializer(serializers.ModelSerializer):


    class Meta:
        model = Movie
        fields='__all__'



class ArticleListSerializer(serializers.ModelSerializer):
    movie_like= serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields='__all__'



class MovieCommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email
    
    class Meta:
        model = Comment
        fields='__all__'


class ArticleDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields='__all__'


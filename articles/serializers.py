from rest_framework import serializers

from articles.models import Movie,Comment
from users.models import User



class ArticleSerializer(serializers.ModelSerializer):


    class Meta:
        model = Movie
        fields='__all__'



class MovieLikeUserNickname(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nickname',]


class ArticleListSerializer(serializers.ModelSerializer):
    movie_like = MovieLikeUserNickname(many=True)

    class Meta:
        model = Movie
        fields='__all__'



class MovieSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email
    
    class Meta:
        model = Movie
        fields='__all__'


class ArticleDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields='__all__'


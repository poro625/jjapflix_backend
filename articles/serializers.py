from rest_framework import serializers

from articles.models import Movie,Comment

class ArticleSerializer(serializers.ModelSerializer):


    class Meta:
        model = Comment
        fields='__all__'



class ArticleListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    comment_like = serializers.StringRelatedField(many=True)


    def get_user(self, obj):
        return obj.user.email


    class Meta:
        model = Comment
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


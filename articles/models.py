from django.db import models
from users.models import User

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    comment_like = models.ManyToManyField(User, related_name="like_comment")








class Movie(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    moive_id = models.CharField()
    image = models.URLField()
    title = models.CharField()
    release_year = models.DecimalField()
    rating = models.CharField()
    duration = models.CharField()
    description = models.TextField()
    movie_like = models.ManyToManyField(Comment, related_name="like_movie")



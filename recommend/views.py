import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from articles.models import Movie, Category
from django.db.models import Max

trends = pd.read_csv('recommend/trend.csv')
netflix = pd.read_csv('recommend/netflix.csv')

movie_ratings = pd.merge(trends, netflix, on='movie_id')

print(movie_ratings)

user_title = movie_ratings.pivot_table('rating_x', index='title', columns='user_id')
user_title = user_title.fillna(0)

item_based_collab = cosine_similarity(user_title, user_title)
item_based_collab = pd.DataFrame(item_based_collab, index=user_title.index, columns=user_title.index)

def item_based_filtering(request):
    if request.method == 'GET':
        movie_list = item_based_collab['더 요트'].sort_values(ascending=False)[:10]
        print(movie_list)
        return movie_list
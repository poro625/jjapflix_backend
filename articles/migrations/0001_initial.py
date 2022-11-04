
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.CharField(max_length=50)),
                ('image', models.URLField()),
                ('original_title', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('release_year', models.DecimalField(decimal_places=0, max_digits=10)),
                ('rating', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('category', models.ManyToManyField(related_name='movie', to='articles.category')),
                ('movie_like', models.ManyToManyField(blank=True, related_name='like_movie', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rating', models.CharField(blank=True, max_length=10)),
                ('comment_like', models.ManyToManyField(blank=True, related_name='like_comment', to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie_comment', to='articles.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

from bs4 import BeautifulSoup
from sorl.thumbnail import get_thumbnail
from django.utils.text import Truncator
from django.utils.html import strip_tags

from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    def to_representation(self, post):
        imgs = BeautifulSoup(post.content, "html.parser").find_all("img")
        thumbnail = get_thumbnail(imgs[0].get("src"), "100x100", crop='center', quality=99).url if imgs else None

        post_dict = {
            "id": post.pk,
            "title": post.title,
            "content": Truncator(strip_tags(post.content)).words(50),
            "createdAt": post.created_date.strftime("%Y.%m.%d %H:%M:%S"),
            "category": post.category.name,
            "tags": [post.name for post in post.tags.all()],
            "thumbnail": thumbnail,
        }
        return post_dict

    class Meta:
        model = Post
        #fields = ('pk', 'title', 'content')

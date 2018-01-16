from django.utils.text import Truncator
from django.utils.html import strip_tags

from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    def to_representation(self, post):
        post_dict = {
            "id": post.pk,
            "title": post.title,
            "content": Truncator(strip_tags(post.content)).words(20)
        }
        return post_dict

    class Meta:
        model = Post
        #fields = ('pk', 'title', 'content')

from rest_framework import viewsets
from rest_framework.response import Response

from blog.models import Post
from api.rest_framework.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, pk=None):
        post_dict = {}
        post = Post.objects.filter(pk=pk).first()

        if post is not None:
            title = post.title
            content = post.content
            category = post.category.name if post.category else None
            created_date = post.created_date.strftime("%Y년 %m월 %d일 %H:%M")
            tags = [tag.name for tag in post.tags.all()]

            post_dict.update({
                "id": post.pk,
                "title": title,
                "content": content,
                "category": category,
                "createdAt": created_date,
                "tags": tags,
            })

        return Response(post_dict, status=200)

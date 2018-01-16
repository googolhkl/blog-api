from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from blog.models import Post
from api.rest_framework.serializers import PostSerializer
class PostPagination(PageNumberPagination):
    page_size = 10

class PostViewSet(viewsets.ModelViewSet):
    pagination_class = PostPagination

    def list(self, request):
        try:
            queryset = Post.objects.all()

            query_type = request.GET.get("type")
            type_name = request.GET.get("name")

            if query_type and type_name:
                if query_type == "category":
                    queryset = queryset.filter(category__name__icontains=type_name)
                elif query_type == "tag":
                    queryset = queryset.filter(tags__name__icontains=type_name)

            queryset = queryset.order_by("-pk")
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = PostSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
        except Exception as e:
            return Response({}, status=400)

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

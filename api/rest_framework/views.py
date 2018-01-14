from rest_framework import viewsets
from rest_framework.response import Response

from blog.models import Post
from api.rest_framework.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset = Post.objects.filter(pk=291)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

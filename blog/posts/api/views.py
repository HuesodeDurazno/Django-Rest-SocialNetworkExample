import imp
from rest_framework.viewsets import ModelViewSet
from posts.api.serializer import PostSerializer
from posts.api.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from posts.models import Post

class PostAPIViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
from sys import prefix
from rest_framework.routers import DefaultRouter
from categories.api.views import CategoryAPIViewSet

router_categories = DefaultRouter()
router_categories.register(prefix='categories',viewset=CategoryAPIViewSet, basename='categories',)
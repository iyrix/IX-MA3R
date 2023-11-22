from django.urls import path
from .views import ListViewSet
from rest_framework import routers
from django.urls import path, include

# trailing_slash=False
router = routers.DefaultRouter()
router.register(r'lists', ListViewSet, basename='list')

urlpatterns = [
    path('api/', include(router.urls)),
]
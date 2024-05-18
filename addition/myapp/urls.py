from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InputNumViewSet



router = DefaultRouter()
router.register(r'/api/addition', InputNumViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

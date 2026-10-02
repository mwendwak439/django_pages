# pages/api_urls.py
from rest_framework.routers import DefaultRouter
from .api_views import GreetingViewSet

router = DefaultRouter()
router.register(r'greetings', GreetingViewSet, basename='greeting')

urlpatterns = router.urls
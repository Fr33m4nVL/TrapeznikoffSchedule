from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'', HomeworkViewSet, basename='homeworks')

urlpatterns = router.urls
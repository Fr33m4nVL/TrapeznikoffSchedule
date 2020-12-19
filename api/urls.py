from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'subjects', SubjectViewSet, basename='subjects')
router.register(r'homeworks', HomeworkViewSet, basename='homeworks')
router.register(r'', HomeworkViewSet, basename='homeworks')

urlpatterns = router.urls
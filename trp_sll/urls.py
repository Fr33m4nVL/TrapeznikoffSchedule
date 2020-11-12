from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from schedule import views

router = routers.DefaultRouter()
router.register(r'homeworks', views.HomeworkView, 'homework')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('landing_page.urls')),
]

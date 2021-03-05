
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('manga', views.MangaViewSet, basename='Bid')

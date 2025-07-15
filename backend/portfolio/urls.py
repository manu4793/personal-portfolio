from django.urls import path, include
from rest_framework import routers
from .views import ProjectViewSet  # Make sure you have this view!
from .views import run_box_ecm_script

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('run-box-ecm/', run_box_ecm_script, name='run-box-ecm'),
]

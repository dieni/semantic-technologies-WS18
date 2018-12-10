from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('controllers', views.ControllerView)

urlpatterns = [
	# specify all necessary urls here
	path('', include(router.urls))
]
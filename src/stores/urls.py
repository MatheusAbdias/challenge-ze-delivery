from django.urls import include, path
from rest_framework import routers

from stores.views import StoreViewSet

app_name = "stores"

router = routers.DefaultRouter()

router.register("", StoreViewSet, basename="stores")

urlpatterns = [
    path("", include(router.urls)),
]

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from stores.filters import RegionFilter
from stores.models import Store
from stores.serializers import StoreSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [AllowAny]
    filter_backends = [RegionFilter]

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data"), list):
            kwargs["many"] = True

        return super().get_serializer(*args, **kwargs)

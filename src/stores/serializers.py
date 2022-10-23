from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometryField

from stores.models import Store


class StoreListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        stores = [Store(**store) for store in validated_data]
        Store.objects.bulk_create(stores)

        return stores


class StoreSerializer(GeoFeatureModelSerializer):
    coverage_area = GeometryField(precision=2, remove_duplicates=True)

    class Meta:
        model = Store
        geo_field = "coverage_area"
        fields = [
            "id",
            "trading_name",
            "owner_name",
            "document",
            "coverage_area",
            "address",
            "created",
            "modified",
        ]
        list_serializer_class = StoreListSerializer

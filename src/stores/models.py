from django.contrib.gis.db import models
from model_utils.models import TimeStampedModel


class Store(TimeStampedModel):
    trading_name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    document = models.CharField(max_length=255, unique=True)
    coverage_area = models.MultiPolygonField()
    address = models.PointField()

    class Meta:
        ordering = ["-created"]
        verbose_name = "Store"
        verbose_name_plural = "Stores"

    def __str__(self) -> str:
        return f"{self.trading_name}-{self.owner_name}"

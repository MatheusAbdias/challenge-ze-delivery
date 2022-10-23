# Generated by Django 4.1 on 2022-08-28 03:23

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Store",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("trading_name", models.CharField(max_length=255)),
                ("owner_name", models.CharField(max_length=255)),
                ("document", models.CharField(max_length=255, unique=True)),
                (
                    "coverage_area",
                    django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
                ),
                ("address", django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                "verbose_name": "Store",
                "verbose_name_plural": "Stores",
                "ordering": ["-created"],
            },
        ),
    ]
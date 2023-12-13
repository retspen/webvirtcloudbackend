# Generated by Django 4.2.3 on 2023-12-13 18:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("region", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Compute",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ("name", models.CharField(max_length=255)),
                (
                    "arch",
                    models.CharField(
                        choices=[("x86_64", "X64"), ("aarch64", "ARM64")], default="x86_64", max_length=50
                    ),
                ),
                ("description", models.TextField()),
                ("hostname", models.CharField(max_length=255)),
                ("token", models.CharField(max_length=255)),
                ("is_active", models.BooleanField(default=True, verbose_name="Active")),
                ("is_deleted", models.BooleanField(default=False, verbose_name="Deleted")),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("deleted", models.DateTimeField(blank=True, null=True)),
                ("region", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="region.region")),
            ],
            options={
                "verbose_name": "Compute",
                "verbose_name_plural": "Computes",
                "ordering": ["-id"],
            },
        ),
    ]

# Generated by Django 4.2.3 on 2023-08-20 19:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("virtance", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="virtancehistory",
            name="event",
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name="virtancehistory",
            name="message",
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-17 18:22

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Stadium",
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
                ("name", models.CharField(max_length=50, unique=True)),
                ("location", models.CharField(max_length=50)),
                ("capacity", models.IntegerField()),
                ("brokeground", models.DateField()),
                ("architect", models.CharField(max_length=20)),
                ("guid", models.CharField(max_length=36, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Team",
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
                ("name", models.CharField(max_length=50, unique=True)),
                ("nicknames", models.CharField(max_length=50, null=True)),
                ("shortname", models.CharField(max_length=50, null=True)),
                ("founded", models.DateField()),
                ("stadium", models.CharField(max_length=20)),
                ("website", models.CharField(max_length=50)),
                ("league", models.CharField(max_length=20)),
                ("description", models.TextField()),
                ("guid", models.CharField(max_length=36, unique=True)),
            ],
        ),
    ]

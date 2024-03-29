# Generated by Django 4.2.3 on 2023-07-17 18:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("premier_league", "0004_alter_news_author_alter_news_team"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("guid", models.CharField(max_length=36, unique=True)),
            ],
        ),
    ]

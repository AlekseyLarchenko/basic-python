# Generated by Django 4.2.3 on 2023-07-17 18:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("premier_league", "0005_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="teams",
            field=models.ManyToManyField(related_name="users", to="premier_league.team"),
        ),
    ]

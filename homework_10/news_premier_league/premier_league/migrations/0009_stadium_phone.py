# Generated by Django 4.2.3 on 2023-07-25 18:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("premier_league", "0008_comments_author_comments_news"),
    ]

    operations = [
        migrations.AddField(
            model_name="stadium",
            name="phone",
            field=models.CharField(max_length=20, null=True),
        ),
    ]

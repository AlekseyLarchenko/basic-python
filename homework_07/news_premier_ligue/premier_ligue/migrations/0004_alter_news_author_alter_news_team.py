# Generated by Django 4.2.3 on 2023-07-17 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("premier_ligue", "0003_author_news"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="news",
                to="premier_ligue.author",
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="team",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="news",
                to="premier_ligue.team",
            ),
        ),
    ]

# Generated by Django 3.0.5 on 2020-08-10 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_titles', '0003_title_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='rating',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]

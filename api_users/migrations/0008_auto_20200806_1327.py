# Generated by Django 3.0.5 on 2020-08-06 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_users', '0007_auto_20200806_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
    ]

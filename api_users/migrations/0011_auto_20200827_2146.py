# Generated by Django 3.0.5 on 2020-08-27 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_users', '0010_auto_20200814_1313'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'user'), ('moderator', 'moderator'), ('admin', 'admin')], default='user', max_length=25),
        ),
    ]

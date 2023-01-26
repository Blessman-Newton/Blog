# Generated by Django 4.1.3 on 2023-01-15 23:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_alter_post_fullname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='fullname',
        ),
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
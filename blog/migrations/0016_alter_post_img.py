# Generated by Django 4.1.3 on 2023-03-03 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(height_field=30, upload_to='images', width_field=70),
        ),
    ]
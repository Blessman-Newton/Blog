# Generated by Django 4.1.3 on 2023-01-15 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_body_text_alter_post_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='username',
            new_name='fullname',
        ),
    ]

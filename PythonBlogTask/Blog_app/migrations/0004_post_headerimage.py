# Generated by Django 4.0.2 on 2022-02-17 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_app', '0003_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='headerimage',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]

# Generated by Django 4.0.1 on 2022-02-03 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='landing',
            name='image_url',
        ),
        migrations.AddField(
            model_name='landing',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
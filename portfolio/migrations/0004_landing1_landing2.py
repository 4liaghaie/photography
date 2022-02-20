# Generated by Django 4.0 on 2022-02-20 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_fashion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Landing1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Landing2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='')),
            ],
        ),
    ]
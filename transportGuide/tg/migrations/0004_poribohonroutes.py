# Generated by Django 3.2.9 on 2021-12-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg', '0003_userprefhist'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoribohonRoutes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poribohonName', models.CharField(max_length=250)),
                ('fullRoute', models.TextField()),
            ],
        ),
    ]
# Generated by Django 4.2 on 2023-04-11 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_short_description',
            field=models.CharField(default='Enter A short Description', max_length=255),
        ),
    ]

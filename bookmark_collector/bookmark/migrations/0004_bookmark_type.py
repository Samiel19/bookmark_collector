# Generated by Django 4.2.7 on 2023-11-14 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0003_bookmark_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='type',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]

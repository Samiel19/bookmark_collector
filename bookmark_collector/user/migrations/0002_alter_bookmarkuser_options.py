# Generated by Django 4.2.7 on 2023-11-16 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmarkuser',
            options={'ordering': ('-date_joined',), 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]
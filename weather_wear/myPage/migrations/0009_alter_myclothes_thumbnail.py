# Generated by Django 3.2.3 on 2021-07-03 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myPage', '0008_alter_myclothes_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myclothes',
            name='thumbnail',
            field=models.ImageField(blank=True, default="{%static 'images/blank.png' %}", null=True, upload_to='images'),
        ),
    ]

# Generated by Django 3.2.3 on 2021-07-04 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myPage', '0011_alter_myclothes_weather'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myclothes',
            name='weather',
            field=models.CharField(choices=[('맑음', 'sunny'), ('흐림', 'cloud'), ('비', 'rain'), ('눈', 'snow')], default='', max_length=20),
        ),
    ]

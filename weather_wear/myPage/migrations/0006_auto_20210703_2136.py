# Generated by Django 3.2.3 on 2021-07-03 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myPage', '0005_myclothes_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myclothes',
            name='thumbnail',
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('my_clothes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myPage.myclothes')),
            ],
        ),
    ]

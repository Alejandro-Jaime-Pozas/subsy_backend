# Generated by Django 5.0.6 on 2024-11-05 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite_num',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='domain',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
# Generated by Django 2.2.6 on 2019-11-26 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missao', '0007_auto_20191025_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missoes',
            name='patrocinador',
            field=models.TextField(blank=True, null=True),
        ),
    ]

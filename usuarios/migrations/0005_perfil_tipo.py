# Generated by Django 2.2.6 on 2019-11-26 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20191122_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='tipo',
            field=models.IntegerField(null=True),
        ),
    ]

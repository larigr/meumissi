# Generated by Django 2.2.6 on 2019-10-25 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missao', '0006_remove_missoes_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='missoes',
            name='arquivo',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='missoes',
            name='cod_premio',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='missoes',
            name='isTerminada',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='missoes',
            name='isTrocado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='missoes',
            name='patrocinador',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='missoes',
            name='premio',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]

# Generated by Django 2.2.6 on 2019-10-13 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField(max_length=1000)),
                ('data_publi', models.DateTimeField()),
                ('resumo', models.TextField(max_length=200)),
                ('autor', models.CharField(max_length=30)),
            ],
        ),
    ]

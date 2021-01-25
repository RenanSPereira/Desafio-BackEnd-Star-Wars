# Generated by Django 3.1.5 on 2021-01-24 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('climate', models.TextField(max_length=20)),
                ('terrain', models.TextField(max_length=20)),
                ('films_qty', models.PositiveIntegerField()),
            ],
        ),
    ]

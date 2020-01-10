# Generated by Django 3.0 on 2020-01-04 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Product Name')),
                ('description', models.CharField(max_length=500, verbose_name='Description')),
                ('create_at', models.DateTimeField(verbose_name='Created Date')),
            ],
        ),
    ]
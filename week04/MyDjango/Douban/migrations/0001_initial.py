# Generated by Django 2.2.13 on 2020-12-20 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('stars', models.IntegerField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('mid', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]

# Generated by Django 3.0.8 on 2020-09-08 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200901_0450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topic_id', models.AutoField(primary_key=True, serialize=False)),
                ('topic_name', models.CharField(max_length=80)),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='image')),
                ('date', models.DateField()),
            ],
        ),
    ]
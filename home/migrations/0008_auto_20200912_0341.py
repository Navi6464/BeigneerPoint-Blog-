# Generated by Django 3.0.8 on 2020-09-12 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_blogcomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='parent',
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='post_name',
            field=models.CharField(default='', max_length=90),
            preserve_default=False,
        ),
    ]

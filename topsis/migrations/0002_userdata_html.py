# Generated by Django 4.0.6 on 2022-08-07 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topsis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='html',
            field=models.TextField(default=None, null=True),
        ),
    ]

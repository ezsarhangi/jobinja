# Generated by Django 4.0.5 on 2022-06-24 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_editprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='editprofile',
            name='city',
            field=models.CharField(default='tehran', max_length=11),
        ),
        migrations.AddField(
            model_name='editprofile',
            name='country',
            field=models.CharField(default='Iran', max_length=11),
        ),
    ]

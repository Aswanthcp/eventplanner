# Generated by Django 4.2 on 2023-06-07 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_alter_itemuserrent_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventuserbook',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='itemuserrent',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.2.7 on 2024-02-04 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='contact_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

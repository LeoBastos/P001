# Generated by Django 2.2.7 on 2019-11-12 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20191112_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='ano',
            field=models.CharField(max_length=10),
        ),
    ]

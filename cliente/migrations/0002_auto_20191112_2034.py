# Generated by Django 2.2.7 on 2019-11-12 23:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='estado',
        ),
        migrations.AddField(
            model_name='cliente',
            name='ano',
            field=models.CharField(default=12, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='carro',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='combustivel',
            field=models.IntegerField(choices=[('A', 'Alcool'), ('G', 'Gasolina'), ('D', 'Diesel'), ('F', 'Flex')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='cliente',
            name='fabricante',
            field=models.IntegerField(choices=[('Volkswagen', 'volkswagen'), ('FIAT', 'FIAT'), ('Chevrolet', 'Chevrolet'), ('General Motors', 'General Motors'), ('Hyundai-Kia', 'Hyundai-Kia'), ('Ford Motor', 'Ford Motor'), ('Renault-Nissan', 'Renault-Nissan'), ('Honda Motor', 'Honda Motor'), ('Mercedes', 'Mercedes')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='modelo',
            field=models.IntegerField(choices=[('H', 'Hatch'), ('S', 'Sedã'), ('U', 'SUV'), ('V', 'Van'), ('C', 'Picape')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='motor',
            field=models.IntegerField(choices=[('1.0', '1.0'), ('1.4', '1.4'), ('1.8', '1.8'), ('2.0', '2.0')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='pintura',
            field=models.IntegerField(choices=[('Azul', 'Azul'), ('Amarelo', 'Amarelo'), ('Branco', 'Branco'), ('Cinza', 'Cinza'), ('Prata', 'Prata'), ('Preto', 'Preto'), ('Dourado', 'Dourado'), ('Vermelho', 'Vermelho')], default=1),
            preserve_default=False,
        ),
    ]
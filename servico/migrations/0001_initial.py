# Generated by Django 2.2.7 on 2019-11-12 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0004_auto_20191112_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(max_length=300)),
                ('solucao', models.TextField(max_length=300)),
                ('status', models.BooleanField(default=False)),
                ('pecas', models.CharField(max_length=80)),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carros', to='cliente.Cliente')),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nomes', to='cliente.Cliente')),
            ],
        ),
    ]
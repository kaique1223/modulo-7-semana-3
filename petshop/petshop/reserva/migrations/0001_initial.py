# Generated by Django 4.2.6 on 2023-11-14 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('data', models.DateField(help_text='dd/mm/aaaa', verbose_name='data')),
                ('turno', models.IntegerField(choices=[('MANHÃ', 'Manhã'), ('TARDE', 'Tarde')], max_length=10, verbose_name='turno')),
                ('tamanho', models.IntegerField(choices=[(0, 'PEQUENO'), (1, 'MEDIO'), (2, 'GRANDE')], verbose_name='tamanha')),
                ('observaçoes', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Reserva De Banho',
                'verbose_name_plural': 'Reservas De Banhos',
            },
        ),
    ]

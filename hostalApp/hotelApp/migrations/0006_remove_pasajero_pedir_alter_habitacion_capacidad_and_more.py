# Generated by Django 4.2.6 on 2023-12-03 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotelApp', '0005_habitacion_idhotel_alter_habitacion_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pasajero',
            name='pedir',
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='capacidad',
            field=models.IntegerField(verbose_name='Capacidad de la habitacion'),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='cocina',
            field=models.BooleanField(verbose_name='¿Hay cocina?'),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='disponibilidad',
            field=models.BooleanField(verbose_name='¿Esta disponible?'),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='habitacion',
            field=models.CharField(max_length=255, verbose_name='Numero de la habitacion'),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='idHotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotelApp.hotel', verbose_name='Dirección del Hotel'),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio de la habitacion'),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='terraza',
            field=models.BooleanField(verbose_name='¿Hay terraza?'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='direccionHotel',
            field=models.CharField(max_length=255, verbose_name='Direccion del hotel'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='habitacionHotel',
            field=models.IntegerField(verbose_name='Numero de habitaciones'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='nombreHotel',
            field=models.CharField(max_length=255, verbose_name='Nombre del hotel'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='numberHotel',
            field=models.IntegerField(verbose_name='Numero de la direccion del hotel'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='phoneHotel',
            field=models.CharField(max_length=15, verbose_name='Numero de telefono del hotel'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='tarifaHotel',
            field=models.FloatField(verbose_name='Tarifa del hotel'),
        ),
        migrations.AlterField(
            model_name='pasajero',
            name='apellidoClient',
            field=models.CharField(max_length=255, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='pasajero',
            name='fonoClient',
            field=models.CharField(max_length=15, verbose_name='Numero telefonico'),
        ),
        migrations.AlterField(
            model_name='pasajero',
            name='llegadaClient',
            field=models.CharField(max_length=23, verbose_name='Día de llega'),
        ),
        migrations.AlterField(
            model_name='pasajero',
            name='nombreClient',
            field=models.CharField(max_length=255, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='pasajero',
            name='rutClient',
            field=models.CharField(max_length=15, verbose_name='Rut'),
        ),
        migrations.AlterField(
            model_name='pasajero',
            name='salidaClient',
            field=models.CharField(max_length=23, verbose_name='Dia de salida'),
        ),
        migrations.AlterField(
            model_name='pasajerohabitacion',
            name='habitacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotelApp.habitacion', verbose_name='Numero de habitacion'),
        ),
        migrations.AlterField(
            model_name='pasajerohabitacion',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotelApp.hotel', verbose_name='Direccion'),
        ),
        migrations.AlterField(
            model_name='pasajerohabitacion',
            name='pasajero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotelApp.pasajero', verbose_name='Nombre del Pasajero'),
        ),
    ]

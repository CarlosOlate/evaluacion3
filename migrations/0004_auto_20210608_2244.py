# Generated by Django 3.2.4 on 2021-06-09 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCommerse', '0003_niveleducacional_pais_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fechaNac',
            field=models.DateField(),
        ),
    ]
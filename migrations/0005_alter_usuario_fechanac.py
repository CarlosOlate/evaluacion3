# Generated by Django 3.2.4 on 2021-06-09 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCommerse', '0004_auto_20210608_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='fechaNac',
            field=models.DateField(max_length=50),
        ),
    ]

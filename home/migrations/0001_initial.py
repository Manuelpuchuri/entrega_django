# Generated by Django 4.1.2 on 2022-10-05 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('Apellido', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
            ],
        ),
    ]

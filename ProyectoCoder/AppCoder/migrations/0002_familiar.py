# Generated by Django 4.1.1 on 2022-10-03 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('Salario', models.IntegerField()),
                ('fechadeNacimiento', models.DateField()),
            ],
        ),
    ]

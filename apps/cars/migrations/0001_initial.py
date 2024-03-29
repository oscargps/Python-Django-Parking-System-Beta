# Generated by Django 2.2 on 2019-04-09 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('placa', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=10)),
                ('fecha_in', models.DateField()),
                ('fecha_out', models.DateField()),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='owners.Owner')),
            ],
        ),
    ]

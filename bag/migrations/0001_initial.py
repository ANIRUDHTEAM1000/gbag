# Generated by Django 3.2.7 on 2021-09-12 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guser',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='items',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('quantity', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bag.guser')),
            ],
        ),
    ]

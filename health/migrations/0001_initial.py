# Generated by Django 3.2.12 on 2022-07-12 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iduser', models.IntegerField()),
                ('idservice', models.IntegerField()),
                ('creation', models.DateField()),
                ('note', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
# Generated by Django 4.0.5 on 2022-06-14 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='stname',
            field=models.CharField(max_length=15),
        ),
    ]
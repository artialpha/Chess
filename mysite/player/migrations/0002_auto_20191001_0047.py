# Generated by Django 2.2.5 on 2019-09-30 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='date_of_birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='player',
            name='surname',
            field=models.CharField(max_length=50),
        ),
    ]
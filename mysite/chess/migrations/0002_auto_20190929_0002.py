# Generated by Django 2.2.5 on 2019-09-28 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chess', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chessopening',
            name='algebraic_notation',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='chessopening',
            name='epd',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
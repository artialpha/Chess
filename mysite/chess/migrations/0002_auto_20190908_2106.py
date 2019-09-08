# Generated by Django 2.2.5 on 2019-09-08 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chess', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChessOpening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_opening', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('eco', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('moves', models.TextField()),
                ('number', models.DecimalField(decimal_places=0, max_digits=2)),
                ('description', models.TextField()),
                ('chess_opening', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chess.ChessOpening')),
            ],
        ),
        migrations.DeleteModel(
            name='ChessOpenings',
        ),
    ]

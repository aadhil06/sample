# Generated by Django 4.1 on 2022-08-16 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='desc',
        ),
        migrations.AddField(
            model_name='note',
            name='mail',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='note',
            name='usn',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='note',
            name='age',
            field=models.IntegerField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='note',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
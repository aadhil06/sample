# Generated by Django 4.1 on 2022-08-16 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummy', '0002_remove_note_desc_note_mail_note_usn_alter_note_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='age',
            field=models.IntegerField(),
        ),
    ]
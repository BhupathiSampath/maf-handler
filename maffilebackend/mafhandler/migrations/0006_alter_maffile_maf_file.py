# Generated by Django 3.2.7 on 2021-09-09 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mafhandler', '0005_alter_maffile_maf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maffile',
            name='maf_file',
            field=models.FileField(max_length=300, unique=True, upload_to=''),
        ),
    ]
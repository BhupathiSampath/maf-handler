# Generated by Django 3.2.7 on 2021-09-09 08:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mafhandler', '0007_alter_maffile_maf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maffile',
            name='maf_file',
            field=models.FileField(max_length=300, upload_to='', validators=[django.core.validators.FileExtensionValidator(['xlsx', 'pptx', 'docx', 'xls'])]),
        ),
    ]

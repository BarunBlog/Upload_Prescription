# Generated by Django 3.2.5 on 2021-07-17 10:06

from django.db import migrations, models
import upload_prescription_api.validators


class Migration(migrations.Migration):

    dependencies = [
        ('upload_prescription_api', '0002_alter_upload_prescription_delivary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_prescription',
            name='prescription_file',
            field=models.FileField(upload_to='prescription/', validators=[upload_prescription_api.validators.validate_file_extension]),
        ),
    ]
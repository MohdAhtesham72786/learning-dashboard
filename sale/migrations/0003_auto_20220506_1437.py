# Generated by Django 3.2.5 on 2022-05-06 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0002_rename_form_date_student_form_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='form_data',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]

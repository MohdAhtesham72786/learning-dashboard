# Generated by Django 3.2.5 on 2022-05-13 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0007_alter_student_form_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='form_date',
            field=models.DateField(null=True),
        ),
    ]
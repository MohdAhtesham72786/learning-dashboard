# Generated by Django 3.2.5 on 2022-05-12 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0006_auto_20220512_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='form_date',
            field=models.DateField(default=0, null=True),
        ),
    ]

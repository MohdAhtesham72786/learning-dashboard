# Generated by Django 3.2.5 on 2022-05-14 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0008_alter_student_form_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='blog_image')),
                ('tags', models.CharField(blank=True, max_length=255, null=True)),
                ('body', models.TextField()),
                ('date_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Blogs',
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('amount_type', models.CharField(default='Percentage', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Coupons',
            },
        ),
        migrations.CreateModel(
            name='MetaTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sale.blog')),
                ('cupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sale.coupon')),
            ],
            options={
                'verbose_name_plural': 'Meta Tags',
            },
        ),
    ]
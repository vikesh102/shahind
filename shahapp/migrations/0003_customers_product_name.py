# Generated by Django 3.2.9 on 2021-12-20 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shahapp', '0002_alter_customers_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='Product_Name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-16 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_shop_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='category',
            field=models.CharField(default='', max_length=10),
        ),
    ]

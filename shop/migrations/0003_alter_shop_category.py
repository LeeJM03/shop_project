# Generated by Django 4.2.7 on 2023-12-16 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_shop_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='category',
            field=models.CharField(choices=[('Outer', 'Outer'), ('Top', 'Top'), ('Bottom', 'Bottom')], default='', max_length=10),
        ),
    ]
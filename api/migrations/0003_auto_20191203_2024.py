# Generated by Django 2.2.7 on 2019-12-03 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20191203_1826'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['nome', 'sobrenome'], 'verbose_name': 'autor'},
        ),
    ]

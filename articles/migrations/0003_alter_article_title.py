# Generated by Django 3.2.4 on 2021-07-03 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210703_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='назва статті'),
        ),
    ]

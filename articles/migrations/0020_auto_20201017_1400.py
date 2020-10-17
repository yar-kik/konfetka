# Generated by Django 3.0.5 on 2020-10-17 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0019_comment_users_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('film', 'Фільми'), ('game', 'Ігри'), ('anime', 'Аніме')], default='film', max_length=16, verbose_name='категорія'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(max_length=20000, verbose_name='текст'),
        ),
    ]

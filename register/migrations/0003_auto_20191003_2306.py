# Generated by Django 2.2.1 on 2019-10-03 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(blank=True, choices=[('在室', '在室'), ('不在', '不在')], max_length=3, verbose_name='user status'),
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-16 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20201111_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='priority',
            field=models.CharField(choices=[('danger', 'high'), ('info', 'normal'), ('success', 'low')], default='danger', max_length=50),
        ),
    ]

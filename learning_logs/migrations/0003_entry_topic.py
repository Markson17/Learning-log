# Generated by Django 3.2.9 on 2021-12-08 02:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='topic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='learning_logs.topic'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-15 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_criterion_max'),
    ]

    operations = [
        migrations.AddField(
            model_name='criterion',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

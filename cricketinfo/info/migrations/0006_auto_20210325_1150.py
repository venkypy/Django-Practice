# Generated by Django 2.0 on 2021-03-25 06:20

from django.db import migrations, models
import info.models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_player2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player2',
            name='dob',
            field=models.DateField(validators=[info.models.dob_validate]),
        ),
    ]

# Generated by Django 4.1.1 on 2022-10-25 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0008_alter_details_time_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='Time_Out',
            field=models.DateTimeField(default=''),
        ),
    ]

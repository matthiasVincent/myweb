# Generated by Django 4.2.3 on 2023-07-12 09:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_message_created_at_alter_message_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 7, 12, 9, 43, 57, 866839)),
        ),
    ]
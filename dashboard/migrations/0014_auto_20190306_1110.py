# Generated by Django 2.1.7 on 2019-03-06 08:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20190306_1028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expensesreportarchive',
            old_name='Month',
            new_name='month',
        ),
        migrations.RenameField(
            model_name='expensesreportarchive',
            old_name='Year',
            new_name='year',
        ),
        migrations.AlterField(
            model_name='expensesreportarchive',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 6, 8, 10, 46, 727551, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='salary',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 6, 8, 10, 46, 726555, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spend',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 6, 8, 10, 46, 727551, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sundry',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 6, 8, 10, 46, 726555, tzinfo=utc)),
        ),
    ]

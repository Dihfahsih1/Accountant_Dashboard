# Generated by Django 2.1.7 on 2019-03-09 07:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_auto_20190309_0943'),
    ]

    operations = [
        migrations.CreateModel(
            name='SundryReportArchive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(default=datetime.datetime(2019, 3, 9, 7, 18, 35, 183943, tzinfo=utc))),
                ('Name', models.CharField(default='Name', max_length=100, null=True)),
                ('Amount', models.FloatField(default=0.0, null=True)),
                ('Reason', models.CharField(max_length=100, null=True)),
                ('ReceivedBy', models.CharField(default='Name', max_length=100)),
                ('ApprovedBy', models.CharField(default='Name', max_length=100)),
                ('month', models.CharField(max_length=100, null=True)),
                ('year', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='expensesreportarchive',
            name='ApprovedBy',
            field=models.CharField(default='Name', max_length=100),
        ),
        migrations.AddField(
            model_name='expensesreportarchive',
            name='ReceivedBy',
            field=models.CharField(default='Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='expensesreportarchive',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 9, 7, 18, 35, 183943, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='salary',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 9, 7, 18, 35, 183943, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='salaryreportarchive',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 9, 7, 18, 35, 183943, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spend',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 9, 7, 18, 35, 183943, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sundry',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 9, 7, 18, 35, 183943, tzinfo=utc)),
        ),
    ]

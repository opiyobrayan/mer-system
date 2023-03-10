# Generated by Django 4.1.4 on 2022-12-28 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me_system', '0004_monthlytable'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlytable',
            name='num_planned',
            field=models.IntegerField(default='0', max_length=200, verbose_name='number of planned activities'),
        ),
        migrations.AddField(
            model_name='monthlytable',
            name='planned_list',
            field=models.CharField(default='activityx', max_length=200, verbose_name='planned list'),
        ),
        migrations.AlterField(
            model_name='monthlytable',
            name='num_not_accomplished',
            field=models.IntegerField(max_length=200, verbose_name='unaccomplished number'),
        ),
        migrations.AlterField(
            model_name='monthlytable',
            name='num_reason',
            field=models.IntegerField(max_length=200, verbose_name='number of reasons'),
        ),
    ]

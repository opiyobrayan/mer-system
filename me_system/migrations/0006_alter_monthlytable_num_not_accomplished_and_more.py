# Generated by Django 4.1.4 on 2022-12-30 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('me_system', '0005_monthlytable_num_planned_monthlytable_planned_list_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlytable',
            name='num_not_accomplished',
            field=models.IntegerField(verbose_name='unaccomplished number'),
        ),
        migrations.AlterField(
            model_name='monthlytable',
            name='num_planned',
            field=models.IntegerField(default='0', verbose_name='number of planned activities'),
        ),
        migrations.AlterField(
            model_name='monthlytable',
            name='num_reason',
            field=models.IntegerField(verbose_name='number of reasons'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='your name')),
                ('body', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='me_system.monthlytable')),
            ],
        ),
    ]

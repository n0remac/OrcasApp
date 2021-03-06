# Generated by Django 3.1.4 on 2021-02-25 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ripplerock', '0002_survey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='name',
        ),
        migrations.AddField(
            model_name='survey',
            name='time_on_island',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='age',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='amenities',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='ideal_free_time',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='life_quality',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='noncontentment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='reason',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='want_to_learn',
            field=models.TextField(blank=True),
        ),
    ]

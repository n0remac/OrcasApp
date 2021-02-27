# Generated by Django 3.1.7 on 2021-02-27 00:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.TextField(blank=True, default=' ', null=True)),
                ('page', models.CharField(default=' ', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_on_island', models.CharField(blank=True, default='0 - 1', max_length=200, null=True)),
                ('age', models.IntegerField(blank=True, default=' ', null=True)),
                ('reason', models.TextField(blank=True, default=' ', null=True)),
                ('life_quality', models.TextField(blank=True, default=' ', null=True)),
                ('amenities', models.TextField(blank=True, default=' ', null=True)),
                ('ideal_free_time', models.TextField(blank=True, default=' ', null=True)),
                ('noncontentment', models.TextField(blank=True, default=' ', null=True)),
                ('want_to_learn', models.TextField(blank=True, default=' ', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

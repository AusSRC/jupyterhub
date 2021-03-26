# Generated by Django 3.1.6 on 2021-03-15 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('filename', models.TextField()),
                ('boundary', models.TextField()),
                ('run_date', models.DateTimeField()),
                ('flag_log', models.BinaryField(blank=True, null=True)),
                ('reliability_plot', models.BinaryField(blank=True, null=True)),
                ('log', models.BinaryField(blank=True, null=True)),
                ('parameters', models.JSONField()),
                ('return_code', models.IntegerField(null=True)),
                ('version', models.CharField(blank=True, max_length=512, null=True)),
                ('stdout', models.BinaryField(blank=True, null=True)),
                ('stderr', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'instance',
                'managed': False,
            },
        ),
    ]
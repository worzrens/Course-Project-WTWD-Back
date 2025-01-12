# Generated by Django 3.1.3 on 2020-12-01 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('speciality', models.CharField(choices=[('MA', 'Mathematics'), ('PH', 'Physics'), ('CH', 'Chemistry'), ('LI', 'Linguistics')], default='LI', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('patronymic', models.CharField(max_length=30)),
                ('subject', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='grades.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('patronymic', models.CharField(max_length=30)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grades.group')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('pupil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grades.pupil')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grades.subject')),
            ],
        ),
    ]

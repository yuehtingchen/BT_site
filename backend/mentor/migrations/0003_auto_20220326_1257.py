# Generated by Django 3.2.12 on 2022-03-26 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
        ('mentor', '0002_auto_20220326_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentors',
            name='uni',
        ),
        migrations.AddField(
            model_name='mentors',
            name='uni',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.uni'),
        ),
    ]

# Generated by Django 2.0 on 2019-03-14 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0007_theme_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='activity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='genre',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='horror',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='numPeople',
            field=models.IntegerField(null=True),
        ),
    ]

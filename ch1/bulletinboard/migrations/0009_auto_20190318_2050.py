# Generated by Django 2.0.5 on 2019-03-18 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bulletinboard', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulletinboard',
            name='password',
            field=models.CharField(default=' ', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='bulletinboard.Bulletinboard'),
            preserve_default=False,
        ),
    ]

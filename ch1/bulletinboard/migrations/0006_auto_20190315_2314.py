# Generated by Django 2.0.5 on 2019-03-15 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletinboard', '0005_delete_faq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletinboard',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
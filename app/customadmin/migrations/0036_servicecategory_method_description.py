# Generated by Django 3.1.4 on 2021-03-31 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0035_auto_20210324_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicecategory',
            name='method_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

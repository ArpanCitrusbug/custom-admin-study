# Generated by Django 3.1.4 on 2020-12-30 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0024_familycode_foundationcode_numbercode_othercode_socialcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familycode',
            name='code',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='foundationcode',
            name='code',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='othercode',
            name='code',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='socialcode',
            name='code',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
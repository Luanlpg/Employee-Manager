# Generated by Django 2.1.5 on 2019-01-31 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190131_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='link',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

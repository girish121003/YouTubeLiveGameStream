# Generated by Django 2.0.8 on 2018-08-13 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stream', '0003_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

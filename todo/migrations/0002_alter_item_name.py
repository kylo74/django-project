# Generated by Django 3.2.13 on 2022-04-29 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

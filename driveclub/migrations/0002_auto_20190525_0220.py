# Generated by Django 2.2.1 on 2019-05-24 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driveclub', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
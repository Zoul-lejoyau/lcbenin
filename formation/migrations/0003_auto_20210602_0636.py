# Generated by Django 3.2.3 on 2021-06-02 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0002_auto_20210501_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='formation',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]

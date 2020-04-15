# Generated by Django 2.1.1 on 2020-03-02 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0003_teachfile_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachfile',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='teachfile',
            name='size',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
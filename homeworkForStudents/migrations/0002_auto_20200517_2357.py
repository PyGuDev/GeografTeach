# Generated by Django 3.0.6 on 2020-05-17 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworkForStudents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answertaskhomework',
            name='answer',
            field=models.TextField(default='', verbose_name='Ответ'),
        ),
        migrations.AddField(
            model_name='answertaskhomework',
            name='img_answe',
            field=models.ImageField(blank=True, upload_to='media/answer/', verbose_name='Изображение'),
        ),
    ]
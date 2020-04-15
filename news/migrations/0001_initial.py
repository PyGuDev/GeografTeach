# Generated by Django 2.2.2 on 2019-08-10 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=30)),
                ('img', models.ImageField(blank=True, upload_to='news/img/')),
                ('text', models.TextField(blank=True, db_index=True)),
                ('textcut', models.TextField(blank=True, db_index=True)),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
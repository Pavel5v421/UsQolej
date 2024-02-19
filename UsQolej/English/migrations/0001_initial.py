# Generated by Django 5.0.1 on 2024-02-03 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnAboutCollege',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt', models.TextField(verbose_name='Homepage: About the College')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
            ],
            options={
                'verbose_name': 'General data',
                'verbose_name_plural': 'General data',
            },
        ),
    ]
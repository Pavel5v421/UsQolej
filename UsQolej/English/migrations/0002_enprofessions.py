# Generated by Django 5.0.1 on 2024-02-03 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('English', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnProfessions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Մասնագիտության անվանում')),
                ('img', models.ImageField(upload_to='Professions imagers', verbose_name='Նկար')),
            ],
            options={
                'verbose_name': 'Մասնագիտություններ',
                'verbose_name_plural': 'Մասնագիտություններ',
            },
        ),
    ]

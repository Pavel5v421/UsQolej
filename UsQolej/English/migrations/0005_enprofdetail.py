# Generated by Django 5.0.1 on 2024-02-03 19:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('English', '0004_alter_enprofessions_img_alter_enprofessions_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnProfDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField(verbose_name='Section information')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enprofdetail', to='English.enprofessions')),
            ],
            options={
                'verbose_name': 'detailed information',
                'verbose_name_plural': 'detailed information',
            },
        ),
    ]

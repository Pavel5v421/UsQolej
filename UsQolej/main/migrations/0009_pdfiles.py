# Generated by Django 5.0.1 on 2024-02-12 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_dimord_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Անունը')),
                ('file', models.FileField(upload_to='pdf', verbose_name='pdf Ֆայլը')),
            ],
            options={
                'verbose_name': 'PDF ֆայլեր',
                'verbose_name_plural': 'PDF ֆայլեր',
            },
        ),
    ]

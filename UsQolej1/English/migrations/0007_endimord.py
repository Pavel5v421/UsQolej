# Generated by Django 5.0.1 on 2024-02-09 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('English', '0006_encontactus_enquestions_enstaffs'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnDimord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Վերնագիր')),
                ('subtitle', models.CharField(max_length=500, verbose_name='Տարբերվող տողը՝ տեքստի սկզբում ')),
                ('text', models.TextField(verbose_name='Տեքստի մնացած հատված')),
                ('img', models.ImageField(null=True, upload_to='dimord', verbose_name='Նկար')),
            ],
            options={
                'verbose_name': 'Դիմորդ',
                'verbose_name_plural': 'Դիմորդ',
            },
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-21 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reclama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='текст рекламы')),
                ('img', models.ImageField(blank=True, default='media/default_cover.png', null=True, upload_to='reclama/%Y/', verbose_name='картинка рекламы')),
            ],
        ),
    ]

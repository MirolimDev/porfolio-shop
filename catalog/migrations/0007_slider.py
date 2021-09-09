# Generated by Django 3.2.6 on 2021-08-24 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20210824_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_title', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=150)),
                ('buttom_title', models.CharField(max_length=150)),
                ('buttom_html', models.TextField()),
                ('clas', models.CharField(max_length=150)),
                ('sort', models.IntegerField()),
            ],
        ),
    ]

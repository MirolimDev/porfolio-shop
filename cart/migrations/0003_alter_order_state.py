# Generated by Django 3.2.6 on 2021-08-29 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_order_orderproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.ImageField(choices=[(1, "To'lov kutulmoqda"), (2, "To'lov bajarildi"), (3, 'Buyurtma bekor qiilindi'), (4, 'Buyurtma yetkazildi')], default=1, upload_to=''),
        ),
    ]

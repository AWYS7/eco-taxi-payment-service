# Generated by Django 5.1.1 on 2024-10-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_cardpaymentmethod_card_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardpaymentmethod',
            name='cvv',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cardpaymentmethod',
            name='is_default',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='cardpaymentmethod',
            name='user_id',
            field=models.BigIntegerField(),
        ),
    ]
# Generated by Django 5.1.1 on 2024-10-17 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_user_cardpaymentmethod_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardpaymentmethod',
            name='card_id',
        ),
        migrations.AddField(
            model_name='cardpaymentmethod',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cardpaymentmethod',
            name='cvv',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='cardpaymentmethod',
            name='expiry_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='cardpaymentmethod',
            name='user_id',
            field=models.CharField(max_length=255),
        ),
    ]

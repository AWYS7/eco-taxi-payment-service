# Generated by Django 5.1.1 on 2024-10-08 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_cardpaymentmethod_user_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardpaymentmethod',
            name='user',
            field=models.CharField(default='default_user', max_length=255),
        ),
    ]

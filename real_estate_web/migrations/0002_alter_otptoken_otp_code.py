# Generated by Django 5.0.1 on 2024-03-07 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate_web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otptoken',
            name='otp_code',
            field=models.CharField(default='6c3c1a', max_length=6),
        ),
    ]
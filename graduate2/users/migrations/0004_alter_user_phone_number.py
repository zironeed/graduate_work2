# Generated by Django 4.2.5 on 2023-09-17 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_phone_number_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(blank=True, max_length=10, null=True, unique=True, verbose_name='User_phone'),
        ),
    ]
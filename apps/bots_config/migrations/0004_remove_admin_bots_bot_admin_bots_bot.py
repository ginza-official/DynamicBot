# Generated by Django 4.2.1 on 2023-05-14 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bots_config', '0003_alter_telegramapi_options_alter_telegramapi_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin_bots',
            name='bot',
        ),
        migrations.AddField(
            model_name='admin_bots',
            name='bot',
            field=models.ManyToManyField(related_name='bot_token', to='bots_config.bot_token'),
        ),
    ]

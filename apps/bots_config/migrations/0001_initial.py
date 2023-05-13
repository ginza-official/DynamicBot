# Generated by Django 4.2.1 on 2023-05-13 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bot_Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('token', models.CharField(blank=True, max_length=200, null=True)),
                ('extra_field', models.CharField(blank=True, max_length=200, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=200, null=True)),
                ('bot_username', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Bot Token',
                'verbose_name_plural': 'Bot Tokens',
                'db_table': 'bot_token',
            },
        ),
        migrations.CreateModel(
            name='Admin_bots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('bot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bots_config.bot_token')),
            ],
            options={
                'verbose_name': 'Admin_bots',
                'verbose_name_plural': 'Admin_bots',
                'db_table': 'admin_bots',
            },
        ),
    ]
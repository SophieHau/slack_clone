# Generated by Django 2.2 on 2019-04-24 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chats.Channel'),
        ),
    ]

# Generated by Django 2.2.16 on 2022-04-20 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20220417_2233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follow',
            options={'ordering': ['id']},
        ),
    ]

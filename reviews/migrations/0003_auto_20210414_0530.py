# Generated by Django 2.2.5 on 2021-04-14 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20210410_0010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='lang_type',
            new_name='language',
        ),
    ]

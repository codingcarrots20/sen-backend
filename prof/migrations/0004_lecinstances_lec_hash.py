# Generated by Django 3.0.7 on 2020-06-21 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0003_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecinstances',
            name='lec_hash',
            field=models.CharField(default=123, max_length=50),
            preserve_default=False,
        ),
    ]

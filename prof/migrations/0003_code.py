# Generated by Django 3.0.7 on 2020-06-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0002_attendancerecord_lecinstances_validtokens'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
            ],
        ),
    ]
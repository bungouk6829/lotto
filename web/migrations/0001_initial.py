# Generated by Django 3.0.5 on 2020-12-22 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='이름')),
                ('phone_number', models.CharField(max_length=20, verbose_name='전화번호')),
            ],
            options={
                'verbose_name': '문의글',
                'verbose_name_plural': '문의글',
                'db_table': 'information',
            },
        ),
    ]
